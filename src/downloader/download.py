import asyncio
import multiprocessing
import random
import threading
import time

import aiofiles as aiofiles
import aiohttp as aiohttp
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL

from src.downloader.fake_ua import random_ua

NUM_OF_THREADS=30

def download_videos(anime_list,duration:int):
    # anime_list=anime_list[:count]
    # if type(anime_list)==dict:
    #     anime_list=anime_list.values()

    thread_list = []
    for anime in anime_list:
        # print(anime.name)
        # print("Proccesing " + anime.name)
        t = threading.Thread(target=download_audio, args=[anime, duration])
        thread_list.append(t)
        t.start()

        while threading.active_count() > NUM_OF_THREADS:  # max thread count (includes parent thread)
            # print('\n == Current active threads ==: ' + str(threading.active_count() - 1))
            time.sleep(1)  # block until active threads are less than 4

    for ex in thread_list:  # wait for all threads to finish
        ex.join()


async def scr_download(anime, ext=".jpg"):
    try:
        anime_scr = random.choice(anime.screenshot)
        headers = {'User-Agent': f'{random_ua}'}
        # headers = {'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://shikimori.me/system/screenshots/original/{anime_scr}" + ext, headers=headers) as response:
                if response.status == 200:
                    filename = f"temp\\Images\\{anime.hex_name}.{ext}"
                    async with aiofiles.open(filename, 'wb') as f:
                        while True:
                            chunk = await response.content.read(8192)
                            if not chunk:
                                break
                            await f.write(chunk)
                elif ext != ".png":
                    print("error on " + anime.name, f"https://shikimori.me/system/screenshots/original/{anime_scr}" + ext)
                    await scr_download(anime, ext=".png")
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

    # Use asyncio.gather for concurrent downloading
    await asyncio.gather(*(download_and_track_progress(anime) for anime in animes))


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
        'outtmpl': f'downloader/%(extractor_key)s/{anime.hex_name}.%(ext)s',
        'quiet':'True',
        'noprogress':'False'
    }

    YoutubeDL(ydl_opts).download([url])
