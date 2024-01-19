import asyncio
import os
import pickle
import random
import subprocess
import threading
import time
import aiofiles as aiofiles
import aiohttp as aiohttp
import requests
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
from src.entities.anime import Anime

from fake_useragent import UserAgent

ua = UserAgent()

scr_url = "https://shikimori.one/api/animes/%s/screenshots"


# async def get_more_screeshots(anime_list,err_count):
#     if err_count>5:
#         return
#     print("exex")
#     headers = {'User-Agent': f'{random_ua}'}
#     for anime in anime_list:
#         response=requests.get(scr_url%anime.id,headers=headers)
#
#         if response.status_code == 200:
#             raw_list = response.json( )
#             scr_list=[]
#             for i in raw_list:
#                 url=i['original']
#                 last_slash_index = url.rfind('/')
#                 dot_index = url.rfind('.')
#                 scr_list.append(url[last_slash_index + 1 : dot_index])
#             anime.screenshot=scr_list
#             print("suc")
#         else:
#             print("Error more scr")
#     await download_screenshots(anime_list)


def resource_path(relative_path):
    import os
    import sys
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


async def scr_download(anime: Anime):
    try:
        anime_scr = random.choice(anime.screenshots)
        last_dot_index = anime_scr.rfind(".")
        scr_ext = anime_scr[last_dot_index:]
        anime.scr_ext = scr_ext

        headers = {'User-Agent': ua.random}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://shikimori.one/system/screenshots/original/{anime_scr}",
                                   headers=headers) as response:
                if response.status == 200:
                    filename = f"temp\\Images\\{anime.hex_name}{scr_ext}"
                    async with aiofiles.open(filename, 'wb') as f:
                        while True:
                            chunk = await response.content.read(8192)
                            if not chunk:
                                break
                            await f.write(chunk)

    except Exception as e:
        print(f"Error downloading for {anime.name}: {e}")


async def download_screenshots(animes):
    total_animes = len(animes)
    completed_animes = 0

    async def download_and_track_progress(anime):
        nonlocal completed_animes
        await scr_download(anime)
        completed_animes += 1
        progress = (completed_animes / total_animes) * 100
        print(f"Progress: {completed_animes}/{total_animes} ({progress:.2f}%)")

    await asyncio.gather(*(download_and_track_progress(anime) for anime in animes))


completed_downloads = 0
lock = threading.Lock()


class Anithemes:
    sorted_list = []

    no_audio_list = []

    anime_audios_dict: dict = {}

    def __init__(self, anime_list):
        self.sort_list(anime_list)

    def sort_list(self, anime_list: list[Anime]):
        file = open('anime_audios.txt', 'rb')
        self.anime_audios_dict = pickle.load(file)
        file.close()

        for anime in anime_list:
            if anime.id in self.anime_audios_dict.keys():

                if 'OP' in self.anime_audios_dict[anime.id]:
                    anime.op_urls.append(self.anime_audios_dict[anime.id]['OP'])
                if 'ED' in self.anime_audios_dict[anime.id]:
                    anime.ed_urls.append(self.anime_audios_dict[anime.id]['ED'])

                self.sorted_list.append(anime)
            else:
                self.no_audio_list.append(anime)

    def anithemes_download(self, thread_num: int, quality: int = 96, audio_type='OP'):
        thread_pool = []
        for anime in self.sorted_list:

            url = random.choice(anime.op_urls if audio_type == 'OP' else anime.ed_urls)
            thread = threading.Thread(target=self.anithemes_download_audio(url, audio_type, anime))
            thread_pool.append(thread)
            thread.start()

            while threading.active_count() > thread_num:
                time.sleep(1)

    def anithemes_download_audio(self, url: str, audio_type: str, anime: Anime):
        start_time = 0
        end_time = 30

        download_dir = 'temp/Audio/'

        response = requests.get(f'https://v.animethemes.moe/{url}')

        if response.status_code == 200:
            with open("video.mp4", "wb") as video_file:
                video_file.write(response.content)

            output_filename = download_dir + anime.hex_name + '_' + audio_type + ".mp3"
            subprocess.run(['ffmpeg/ffmpeg.exe',
                            '-i', 'video.mp4',
                            '-ss', '00:00:00',
                            '-t', f'{end_time}',
                            '-c:a', 'libmp3lame',
                            '-b:a', f'{96}k',
                            output_filename
                            ])

            print(f"Downloaded and trimmed video to {output_filename}")
        else:
            print("Failed to download the video.")


def download_videos(anime_list, duration: int, thead_num: int = os.cpu_count(), quality=60):
    print(f"Downloading {len(anime_list)} videos...")
    thread_list = []
    for anime in anime_list:
        t = threading.Thread(target=download_audio, args=(anime, duration, len(anime_list), quality))
        thread_list.append(t)
        t.start()

        while threading.active_count() > thead_num:
            time.sleep(1)

    for ex in thread_list:
        ex.join()
    print("Downloaded!")


def download_audio(anime, duration, list_len, quality):
    global completed_downloads

    name = anime.name

    videos_search = VideosSearch(name + " anime opening", limit=1)
    url = videos_search.result()["result"][-1]['link']

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': f'{quality}'
        }],
        'postprocessor_args': ['-ss', '00:00:00', '-t', f'{duration}', '-c:a', 'libmp3lame', '-b:a', f'{quality}k'],
        # 'postprocessor_args': ['-ss', '00:00:00', '-t', f'{duration}', '-c:a', 'libmp3lame', '-q:a', f'4'],
        'outtmpl': f'downloader/Youtube/{anime.hex_name}.%(ext)s',
        'quiet': True,
        'noprogress': True,
        'ffmpeg_location': rf"{resource_path('ffmpeg')}"
    }

    try:
        YoutubeDL(ydl_opts).download([url])
        with lock:
            completed_downloads += 1
            print(f"Downloaded {completed_downloads}/{list_len} videos")
    except Exception as e:
        print(f"Error downloading {name}: {e}")


def safe_rename(src, dst):
    try:
        os.rename(src, dst)
    except OSError as e:
        print(f"Error renaming file: {e}")
        time.sleep(1)
        try:
            os.rename(src, dst)
        except OSError as e:
            print(f"Failed to rename file again: {e}")
