import pickle
import random
import re
import time
import requests
from fake_useragent import UserAgent
from src.downloader.fake_ua import random_ua
API_URL="https://shikimori.me/api/"



from src.entities.anime import Anime as animClass

def get_user_score(desc):
    pattern = re.compile(r'>\s*(\d+)\s*<')
    match = pattern.search(desc)
    if match:
        value = match.group(1)
        return value
    else:
        return ""


def getAnimeIds(est_num,shuffle=True):
    anime_list=[]
    anime_num=0
    page=1
    while anime_num<est_num:

        data={
            "page":page,
            "limit":100,
            "target_type":"Anime",
            "order":"popularity",
            "status":"!anons"
        }
        headers = {'User-Agent': f'{random_ua}'}
        try:
            history = requests.get(f"{API_URL}animes",params=data,headers=headers).json()
        except requests.exceptions.JSONDecodeError:
            print(history)
        except requests.exceptions.JSONDecodeError:
            print(history)

        # print(history)
        print(len(history))
        if len(history)==0:
            break
        for i in history:
            anime_list.append(animClass(
                id=i['id'],
                name=i['name'],
                name_rus=i['russian'],
                anime_score=i['score'],
                poster=i['image']['original'],
                kind=i['kind']
            ))
            anime_num += 1
        page+=1

    if shuffle: random.shuffle(anime_list)
    anime_list=anime_list[:est_num]
    return anime_list


# def getAnimeIds(est_num,username,shuffle=True):
#     anime_list=[]
#     anime_num=0
#     page=1
#     while anime_num<est_num:
#
#         data={
#             "page":page,
#             "limit":100,
#             "target_type":"Anime"
#         }
#         history = requests.get(f"{API_URL}animes",params=data,headers=headers).json()
#         #history = requests.get(f"{API_URL}users/{username}/history",params=data,headers=headers).json()
#         print(history)
#         print(len(history))
#         if len(history)==0:
#             break
#         for i in history:
#             if "Просмотрено" in i['description']:
#                 anime_list.append(animClass(
#                     id=i['target']['id'],
#                     name=i['target']['name'],
#                     name_rus=i['target']['russian'],
#                     anime_score=i['target']['score'],
#                     poster=i['target']['image']['original'],
#                     user_score=get_user_score(i['description']),
#                     description=i['description']
#                 ))
#                 anime_num += 1
#         page+=1
#
#     if shuffle: random.shuffle(anime_list)
#     anime_list=anime_list[:est_num]
#     return anime_list

def remove_duplicates(anime_list:list):
    uniq_anim = {}
    sorted_list=[]
    for anime in anime_list:
        # if anime.franchise==None:
        #     uniq_anim[f"{anime.name.replace(' ','_').lower()}"] = anime.id
        # else:
        # print(anime.franchise)
        if anime.franchise!=None:
            uniq_anim[f"{anime.franchise}"] = anime.id

    # for anime in anime_list:
    #     if (anime.id in uniq_anim.values()) and (not anime.id in sorted_list):
    #         sorted_list.append(anime)
    # print(uniq_anim)
    for franchise,anime_id in uniq_anim.items():
        # print(anime_id)
        for anime in anime_list:
            if anime_id==anime.id:
                sorted_list.append(anime)
    return sorted_list


def get_more_screenshots(anime_list:list):
    end=len(anime_list)
    progress=0
    for anime in anime_list:
        screenshots_arr = requests.get(f"{API_URL}animes/{anime.id}/screenshots", headers=headers).json()
        anime.screenshot=[cut_string(i['original']) for i in screenshots_arr]
        time.sleep(0.6)
        progress += 1
        print(f'Getting screenshots {progress}/{end}')

def cut_string(string):
    filename = string.split('/')[-1]  # Extract the filename with extension
    desired_string = filename.split('.')[0]  # Extract the desired portion
    return desired_string

def getAnimeInfo(anime_list:list,allow_duplicates:bool):
    end=len(anime_list)
    progress=0
    for anime in anime_list:
        try:
            animeInfo=requests.get(f"{API_URL}animes/{anime.id}",headers=headers).json()
            #anime.screenshot = random.choice(requests.get(f"{API_URL}animes/{anime.id}/screenshots",headers=headers).json())['original']
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
            anime.kind = animeInfo["kind"]
            anime.franchise = animeInfo["franchise"]
            anime.description=animeInfo['description']
        except IndexError:
            ...
        progress+=1
        print(f'Getting anime infos {progress}/{end}')

        time.sleep(0.6) #avoid api limit




anime_list=getAnimeIds(15000,False)
for i in anime_list:
    print(f'{i.id},',sep='',end='')


# getAnimeInfo(anime_list,False)
# get_more_screenshots(anime_list)
# print("test: ",anime_list[0].genres)


# anime_list=remove_duplicates(anime_list)
# for i,anime in enumerate(anime_list):
#     if ("tv" not in anime.kind) or ("movie" not in anime.kind) or ("ona" not in anime.kind):
#         anime_list.pop(i)

file=open('anime_ids_15000.txt','wb')
pickle.dump(anime_list,file)
file.close()

print("Cached!")

# for anime in anime_list:
#     print(anime.name_rus)