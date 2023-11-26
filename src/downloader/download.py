import asyncio
import os
import random
import threading
import time

import aiofiles as aiofiles
import aiohttp as aiohttp
import requests
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL


from src.downloader.fake_ua import random_ua

NUM_OF_THREADS=12


scr_url="https://shikimori.one/api/animes/%s/screenshots"

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


async def scr_download(anime, ext=".jpg",err=False):
    try:
        anime_scr = random.choice(anime.screenshot)
        headers = {'User-Agent': f'{random_ua}'}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://shikimori.one/system/screenshots/original/{anime_scr}" + ext, headers=headers) as response:
            # async with session.get(f"https://shikimori.me/system/screenshots/original/{anime_scr}" + ext, headers=headers) as response:
                if response.status == 200:
                    filename = f"temp\\Images\\{anime.hex_name}.jpg"
                    async with aiofiles.open(filename, 'wb') as f:
                        while True:
                            chunk = await response.content.read(8192)
                            if not chunk:
                                break
                            await f.write(chunk)
                elif ext == ".jpg" and not err:
                    print("error on " + anime.name, f"https://shikimori.one/system/screenshots/original/{anime_scr}" + ext)
                    await scr_download(anime, ext=".png",err=True)

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


def download_videos(anime_list, duration: int):
    thread_list = []
    for anime in anime_list:
        t = threading.Thread(target=download_audio, args=(anime, duration))
        thread_list.append(t)
        t.start()

        while threading.active_count() > NUM_OF_THREADS:
            time.sleep(1)

    for ex in thread_list:
        ex.join()

def download_audio(anime, duration):
    name = anime.name

    videosSearch = VideosSearch(name + " anime opening", limit=1)
    url = videosSearch.result()["result"][-1]['link']

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '96'
        }],
        'postprocessor_args': ['-ss', '00:00:00', '-t', f'{duration}', '-c:a', 'aac', '-b:a', '96k'],
        'outtmpl': f'downloader/Youtube/{anime.hex_name}.%(ext)s',
        'quiet': True,
        'noprogress': False,
        'ffmpeg_location':rf"{resource_path('ffmpeg')}"

    }

    try:
        YoutubeDL(ydl_opts).download([url])
    except Exception as e:
        print(f"Error downloading {name}: {e}")
        # Optional: Implement a retry mechanism here

def safe_rename(src, dst):
    try:
        os.rename(src, dst)
    except OSError as e:
        print(f"Error renaming file: {e}")
        time.sleep(1)  # Wait for a second and try again
        try:
            os.rename(src, dst)
        except OSError as e:
            print(f"Failed to rename file again: {e}")