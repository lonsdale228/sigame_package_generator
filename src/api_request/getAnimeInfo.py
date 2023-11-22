import random
import time
import re

import requests
from fake_useragent import UserAgent
ua = UserAgent()

# from downloader.download import download_screenshots
# import download_screenshots

from src.entities.anime import anime as animClass

API_URL="https://shikimori.me/api/"



def get_genres():
    user_agent = {'User-Agent': f'{ua.random}'}
    return [genre["name"] for genre in requests.get("https://shikimori.me/api/genres",headers=user_agent,timeout=5).json() if genre["kind"]=="anime"]


def get_user_score(desc):
    pattern = re.compile(r'>\s*(\d+)\s*<')
    match = pattern.search(desc)
    if match:
        value = match.group(1)
        return value
    else:
        return ""

#TODO
def get_anime_desc(anime_list:list):
    ...

headers = {'User-Agent': f'{ua.random}'}
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
        # print(history)
        print(len(history))
        if len(history)==0:
            break
        for i in history:
            if "Просмотрено" in i['description']:
                anime_list.append(animClass(
                    id=i['target']['id'],
                    name=i['target']['name'],
                    name_rus=i['target']['russian'],
                    anime_score=i['target']['score'],
                    poster=i['target']['image']['original'],
                    user_score=get_user_score(i['description'])
                ))
                anime_num += 1
        page+=1

    if shuffle: random.shuffle(anime_list)
    anime_list=anime_list[:est_num]
    return anime_list


def remove_duplicates(anime_list:list):
    uniq_anim = {}
    sorted_list=[]
    for anime in anime_list:
        if anime.franchise==None:
            uniq_anim[f"{anime.name.replace(' ','_').lower()}"] = anime.id
        else:
            uniq_anim[f"{anime.franchise}"] = anime.id

    for anime in anime_list:
        if (anime.id in uniq_anim.values()) and (not anime.id in sorted_list):
            sorted_list.append(anime)
    return sorted_list

def get_anime_info(anime_list:list,allow_duplicates:bool):
    end=len(anime_list)
    progress=0
    for anime in anime_list:
        try:
            animeInfo=requests.get(f"{API_URL}animes/{anime.id}",headers=headers).json()
            #anime.screenshot = random.choice(requests.get(f"{API_URL}animes/{anime.id}/screenshots",headers=headers).json())['original']
            scr_url=random.choice(animeInfo["screenshots"])['original']
            result = re.search(r'[^/]+(?=\.)', scr_url)
            anime.screenshot = [result.group()]
            # print("result group:", anime.screenshot)
            anime.kind=animeInfo["kind"]
            anime.franchise=animeInfo["franchise"]
            anime.genres=[genre["name"] for genre in animeInfo["genres"]]
            # print(anime.id,anime.genres)
            # print(anime.franchise)
            # print(anime.screenshot)
        except requests.exceptions.HTTPError:
            time.sleep(20)
            print("API Request reached, waiting....")
            animeInfo = requests.get(f"{API_URL}animes/{anime.id}", headers=headers).json()
            scr_url = random.choice(animeInfo["screenshots"])['original']
            result = re.search(r'[^/]+(?=\.)', scr_url)
            anime.screenshot = [result.group()]
            # print("result group:", anime.screenshot)

            anime.kind = animeInfo["kind"]
            anime.franchise = animeInfo["franchise"]
        except IndexError:
            ...
        progress+=1
        print(f'Getting anime infos {progress}/{end}')

        time.sleep(0.6) #avoid api limit

    # if not allow_duplicates:
    #     anime_list=remove_duplicates(anime_list)
