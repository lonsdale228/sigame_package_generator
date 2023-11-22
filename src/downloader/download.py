import asyncio
import multiprocessing
import random
import threading
import time

import aiofiles as aiofiles
import aiohttp as aiohttp
import requests
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
from fake_useragent import UserAgent
ua = UserAgent()

NUM_OF_THREADS=30

from multiprocessing import Process, current_process, Pool
# def scr_download(anime,ext=".jpg"):
#     try:
#         anime_scr=random.choice(anime.screenshot)
#         headers = {'User-Agent': f'{ua.random}'}
#         print(f"https://desu.shikimori.me/system/screenshots/original/{anime_scr}"+ext)
#         response = requests.get(f"https://desu.shikimori.me/system/screenshots/original/{anime_scr}"+ext, headers=headers, stream=True)
#         response.raise_for_status()
#
#         filename=f"temp\\Images\\{anime.hex_name}.jpg"
#         print("hex: ", anime.hex_name)
#         with open(filename, 'wb') as f:
#             for chunk in response.iter_content(chunk_size=8192):
#                 f.write(chunk)
#
#
#         print(f"Image saved as {filename}")
#         #print(f"https://shikimori.me{anime.screenshot}", f"temp\\Images\\{anime.hex_name}.jpg")
#     except requests.exceptions.HTTPError:
#         if ext != ".png":
#             print("error on "+anime.name)
#             scr_download(anime,ext=".png")
#
#
#
# def download_screenshots(animes):
#     thread_list = []
#
#     for anime in animes:
#
#         print("amogus: ",anime.screenshot)
#
#     for anime in animes:
#         # print(anime.name)
#         # print("Proccesing " + anime.name)
#         t = threading.Thread(target=scr_download, args=[anime])
#         thread_list.append(t)
#         t.start()
#         while threading.active_count() > NUM_OF_THREADS:  # max thread count (includes parent thread)
#             # print('\n == Current active threads ==: ' + str(threading.active_count() - 1))
#             time.sleep(1)  # block until active threads are less than 4
#     for ex in thread_list:  # wait for all threads to finish
#         ex.join()



# def download_audio(anime, duration):
#     name=anime.name
#
#     videosSearch = VideosSearch(name+" anime opening", limit=1)
#     url = videosSearch.result()["result"][-1]['link']
#
#     ydl_opts = {
#         'format': 'm4a/bestaudio/best',
#         # ️ℹ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#         'postprocessors': [{  # Extract audio using ffmpeg
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'm4a',
#             'preferredquality': '192'
#         }],
#         'postprocessor_args': ['-ss', '00:00:00','-t',f'{duration}','-c:a','aac','-b:a','192k'],
#         'outtmpl': f'downloader/%(extractor_key)s/{anime.hex_name}.%(ext)s'
#     }
#
#     YoutubeDL(ydl_opts).download(url)
#
#
# def download_videos(anime_list,duration:int):
#     # anime_list=anime_list[:count]
#     # if type(anime_list)==dict:
#     #     anime_list=anime_list.values()
#
#     thread_list = []
#     for anime in anime_list:
#         # print(anime.name)
#         # print("Proccesing " + anime.name)
#         t = threading.Thread(target=download_audio, args=[anime, duration])
#         thread_list.append(t)
#         t.start()
#
#         while threading.active_count() > NUM_OF_THREADS:  # max thread count (includes parent thread)
#             # print('\n == Current active threads ==: ' + str(threading.active_count() - 1))
#             time.sleep(1)  # block until active threads are less than 4
#
#     for ex in thread_list:  # wait for all threads to finish
#         ex.join()


async def scr_download(anime, ext=".jpg"):
    try:
        anime_scr = random.choice(anime.screenshot)
        headers = {'User-Agent': f'{ua.random}'}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://shikimori.me/system/screenshots/original/{anime_scr}" + ext, headers=headers) as response:
                if response.status == 200:
                    filename = f"temp\\Images\\{anime.hex_name}.jpg"
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


def download_videos(anime_list, duration: int, num_of_processes: int = multiprocessing.cpu_count()):
    # Create a shared counter initialized to 0
    counter = multiprocessing.Value('i', 0)

    def callback(_):
        # Increment and print the shared counter
        with counter.get_lock():
            counter.value += 1
            print(f"{counter.value}/{len(anime_list)}")

    with Pool(num_of_processes) as pool:
        results = [pool.apply_async(download_audio, args=(anime, duration), callback=callback) for anime in anime_list]

        # wait for processes to complete
        for result in results:
            result.wait()
