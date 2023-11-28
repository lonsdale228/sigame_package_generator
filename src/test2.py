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
# file = open('anime_ids_15000.txt','rb')
# anime_list :list[Anime] = pickle.load(file)
# file.close()
#
# new_dict={}
#
# for anime in anime_list:
#     anime_id=anime.id
#     delattr(anime,"id")
#     new_dict[int(anime_id)] = anime
#
#
# for id, anime in new_dict.items():
#
#     try:
#         anime.name_rus=anime.name_rus.encode().decode('utf-8')
#     except AttributeError:
#         anime.name_rus=anime.name
#
#     for scr in range(len(anime.screenshots)):
#
#         parts = anime.screenshots[scr].split('/')
#         last_part = parts[-1]
#         if '?' in last_part:
#             filename = last_part.split('?')[0]
#         else:
#             filename = last_part
#
#         anime.screenshots[scr]=filename
#
#
#
import pickle
from entities.anime import Anime
new_anime=open('15000_animes.txt','rb')
anime_dict:dict = pickle.load(new_anime)
new_anime.close()

for i, anime in anime_dict.items():
    print(anime.genres)
    anime.genres=[i['name'] for i in anime.genres]

new_new_anime=open('15_000_animes.txt','wb')
pickle.dump(anime_dict,new_new_anime)
new_new_anime.close()