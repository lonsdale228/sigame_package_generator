# import pickle
#
# class Anime:
#     id: int = None
#
#     mal_id: int = None
#     name: str = None
#
#
#
#     name_rus: str = None
#     kind: str = None
#     score: float = None
#     status: str = None
#     episodes: int = None
#
#     poster: str = None
#     screenshots: list[str] = None
#
#     is_censored: bool = None
#
#     genres: list[dict] = None
#
#     studios: list[dict] = None
#     description: str = None
#
#     hex_name:str = None
#     user_score:str = None
#
import pickle
from entities.anime import Anime

file = open('anime_ids_15000_new.txt','rb')
anime_list :list[Anime] = pickle.load(file)
file.close()

new_dict={}

for anime in anime_list:
    anime_id=anime.id
    delattr(anime,"id")
    new_dict[int(anime_id)] = anime


for id, anime in new_dict.items():

    try:
        anime.name_rus=anime.name_rus.encode().decode('utf-8')
    except AttributeError:
        anime.name_rus=anime.name

    for scr in range(len(anime.screenshots)):

        parts = anime.screenshots[scr].split('/')
        last_part = parts[-1]
        if '?' in last_part:
            filename = last_part.split('?')[0]
        else:
            filename = last_part

        anime.screenshots[scr]=filename



# new_anime=open('anime_ids_15000_new.txt','rb')
anime_dict:dict = new_dict
# new_anime.close()


for i, anime in anime_dict.items():
    if anime.characters:
        print(anime.characters)
        if anime.characters:
            start = anime.poster