import os
import threading
import time

import requests
from pytube import YouTube
from youtubesearchpython import VideosSearch
import secrets
import ffmpeg
import subprocess
from yt_dlp import YoutubeDL
import urllib.request
from fake_useragent import UserAgent
ua = UserAgent()

NUM_OF_THREADS=30


def scr_download(anime):
    try:
        headers = {'User-Agent': f'{ua.random}'}
        print(f"https://shikimori.me{anime.screenshot}")
        response = requests.get(f"https://shikimori.me{anime.screenshot}", headers=headers, stream=True)
        response.raise_for_status()

        print(f"https://shikimori.me{anime.screenshot}")
        filename=f"temp\\Images\\{anime.hex_name}.jpg"
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


        print(f"Image saved as {filename}")
        #print(f"https://shikimori.me{anime.screenshot}", f"temp\\Images\\{anime.hex_name}.jpg")
    except requests.exceptions.HTTPError:
        scr_download(anime)

def download_screenshots(animes):
    thread_list = []

    for anime in animes:

        print("amogus: ",anime.screenshot)

    for anime in animes:
        # print(anime.name)
        # print("Proccesing " + anime.name)
        t = threading.Thread(target=scr_download, args=[anime])
        thread_list.append(t)
        t.start()
        while threading.active_count() > NUM_OF_THREADS:  # max thread count (includes parent thread)
            # print('\n == Current active threads ==: ' + str(threading.active_count() - 1))
            time.sleep(1)  # block until active threads are less than 4
    for ex in thread_list:  # wait for all threads to finish
        ex.join()

def download_audio(anime, duration):
    name=anime.name

    videosSearch = VideosSearch(name+" anime opening", limit=1)
    url = videosSearch.result()["result"][-1]['link']

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ️ℹ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192'
        }],
        'postprocessor_args': ['-ss', '00:00:00','-t',f'{duration}','-c:a','aac','-b:a','192k'],
        'outtmpl': f'downloader/%(extractor_key)s/{anime.hex_name}.%(ext)s'
    }

    YoutubeDL(ydl_opts).download(url)


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