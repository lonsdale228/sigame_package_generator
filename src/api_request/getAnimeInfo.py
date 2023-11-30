import random
import time
import re

import requests
from fake_useragent import UserAgent
from src.entities.anime import Anime

ua = UserAgent()

API_URL = "https://shikimori.one/api/"


def get_genres():

    user_agent = {'User-Agent': ua.random}
    # return [genre["name"] for genre in requests.get("https://shikimori.me/api/genres",headers=user_agent,timeout=5).json() if genre["kind"]=="anime"]
    return [genre["name"] for genre in
            requests.get("https://shikimori.one/api/genres", headers=user_agent, timeout=5).json() if
            genre["kind"] == "anime"]


def get_user_score(desc):
    pattern = re.compile(r'>\s*(\d+)\s*<')
    match = pattern.search(desc)
    if match:
        value = match.group(1)
        return value
    else:
        return ""


# TODO
def get_anime_desc(anime_list: list):
    ...





def getAnimeIds(est_num, username, shuffle=True):
    anime_list = []
    anime_num = 0
    page = 1
    while anime_num < est_num:
        headers = {'User-Agent': ua.random}
        data = {
            "page": page,
            "limit": 100,
            "target_type": "Anime"
        }
        history = requests.get(f"{API_URL}users/{username}/history", params=data, headers=headers).json()
        # print(history)
        print(len(history))
        if len(history) == 0:
            break
        for i in history:
            if "Просмотрено" in i['description']:
                anime = Anime()
                anime.id = i['target']['id']
                anime.name = i['target']['name']
                anime.name_rus = i['target']['russian']
                anime.anime_score = i['target']['score']
                anime.poster = i['target']['image']['original']
                anime.user_score = get_user_score(i['description'])

                # print(i['target'])
                anime_list.append(anime)

                anime_num += 1
        page += 1

    if shuffle: random.shuffle(anime_list)
    anime_list = anime_list[:est_num]
    return anime_list

def remove_duplicates(anime_list: list[Anime]):
    unique_franchises = set()

    removed_duplicates = []

    for anime in anime_list:
        if anime.franchise not in unique_franchises and anime.franchise is not None:
            unique_franchises.add(anime.franchise)
            removed_duplicates.append(anime)

    return removed_duplicates


def get_anime_info(anime_list: list):
    end = len(anime_list)
    progress = 0
    for anime in anime_list:
        try:
            headers = {'User-Agent': ua.random}
            animeInfo = requests.get(f"{API_URL}animes/{anime.id}", headers=headers).json()
            scr_url = random.choice(animeInfo["screenshots"])['original']
            result = re.search(r'[^/]+(?=\.)', scr_url)
            anime.screenshots = [result.group()]
            # print("result group:", anime.screenshot)
            anime.kind = animeInfo["kind"]
            anime.franchise = animeInfo["franchise"]
            anime.genres = [genre["name"] for genre in animeInfo["genres"]]
            # print(anime.id,anime.genres)
            # print(anime.franchise)
            # print(anime.screenshot)
        except requests.exceptions.HTTPError:
            time.sleep(20)
            print("API Request reached, waiting....")
            headers = {'User-Agent': ua.random}
            animeInfo = requests.get(f"{API_URL}animes/{anime.id}", headers=headers).json()
            scr_url = random.choice(animeInfo["screenshots"])['original']
            result = re.search(r'[^/]+(?=\.)', scr_url)
            anime.screenshots = [result.group()]
            # print("result group:", anime.screenshot)

            anime.kind = animeInfo["kind"]
            anime.franchise = animeInfo["franchise"]
        except IndexError:
            ...
        progress += 1
        print(f'Getting anime infos {progress}/{end}')

        time.sleep(0.6)  # avoid api limit
