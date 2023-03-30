import random
import time
import re

import requests

from downloader.download import download_screenshots
from entities.anime import anime as animClass


API_URL="https://shikimori.one/api/"

def get_user_score(desc):
    pattern = re.compile(r'>\s*(\d+)\s*<')
    match = pattern.search(desc)
    if match:
        value = match.group(1)
        return value
    else:
        return ""

#TODO
def get_anime_desc(api,animes):
    ...

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
def getAnimeIds(est_num,username,shuffle=True):
    anime_list=[]

    anime_num=0
    page=1
    while anime_num<est_num:
        data={
            "page":page,
            "limit":100,
            "target_type":"Anime"
        }
        history = requests.get(f"{API_URL}users/{username}/history",params=data,headers=headers).json()
        print(len(history))
        for i in history:
            if "Просмотрено" in i['description']:
                anime_list.append(animClass(id=i['target']['id'],name=i['target']['name'],name_rus=i['target']['russian'],anime_score=i['target']['score'],poster=i['target']['image']['original'],user_score=get_user_score(i['description'])))
                anime_num += 1
        page+=1

    if shuffle: random.shuffle(anime_list)
    anime_list=anime_list[0:est_num]
    return anime_list

def getScreenshot(animes):
    end=len(animes)
    progress=0
    for anime in animes:
        try:
            anime.screenshot = random.choice(requests.get(f"{API_URL}animes/{anime.id}/screenshots",headers=headers).json())['original']
            print(anime.screenshot)
        except requests.exceptions.HTTPError:
            time.sleep(20)
            print("API Request reached, waiting....")
            anime.screenshot = random.choice(requests.get(f"{API_URL}animes/{anime.id}/screenshots",headers=headers).json())['original']
        except IndexError:
            ...
        progress+=1
        print(f'Getting screenshots {progress}/{end}')

        time.sleep(0.6) #avoid api limit
    download_screenshots(animes)