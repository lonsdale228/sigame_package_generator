import os
import pickle
import random

import downloader
from api_request.getAnimeInfo import getAnimeIds, getAnimeInfo, get_genres, remove_duplicates
from create_package.create_package import create_package, clear_trash
from create_package.transfer_content import transfer_audio
from downloader.download import download_screenshots, download_videos
from generate.generate_content import create_audio_line, create_round, create_xml_round, create_xml, create_scr_round
from src.api_request.setAnimeCode import set_anime_code
from src.generate import create_dirs
from src.optimizer.sort_anime import sort_by_genres, force_sort_by_genres
from entities.generate import Generate
from entities.anime import anime as animClass


def main(settings:Generate):
    print("boba")

    AUDIO_DURATION:int = settings.op_duration
    ANIME_COUNT:int = settings.num_of_total
    GET_ANIME_MAX:int = settings.num_of_getting
    DOWNLOAD_SCREENSHOTS:bool =settings.scr_round
    DOWNLOAD_AUDIO:bool = settings.op_round
    REMOVE_FRANCHISE_REPEAT:bool = settings.remove_duplicates
    GPT_ROUND:bool=settings.gpt_round
    DESC_ROUND:bool=settings.desc_round
    NICKNAME:str=settings.nickname


    clear_trash()
    create_dirs()

    file = open('anime_dict10000.txt', 'rb')
    anime_dump=pickle.load(file)
    file.close()



    # try:
    anime_list = getAnimeIds(GET_ANIME_MAX,NICKNAME)

    ids = []
    for anime in anime_list:
        print(anime.name)
        ids.append(anime.id)
    print(ids)

    getting_list=[]

    for anime in anime_list:
        try:
            anime=anime_dump[f'{anime.id}']
        except KeyError:
            getting_list.append(anime)


    set_anime_code(anime_list)

    getAnimeInfo(getting_list, REMOVE_FRANCHISE_REPEAT)

    anime_list=anime_list+getting_list

    anime_list=remove_duplicates(anime_list)

    random.shuffle(anime_list)

    # req_genres = settings.selected_genres
    # if settings.rb_req_genres:
    #     anime_list = sort_by_genres(anime_list, req_genres)
    # else:
    #     anime_list=force_sort_by_genres(anime_list,req_genres)



    anime_list = anime_list[:ANIME_COUNT]





    round_list = []

    if DOWNLOAD_AUDIO:
        download_videos(anime_list, AUDIO_DURATION)
        round_audio = create_round(anime_list[:])
        round_list.append(create_xml_round(round_audio, "audio"))
    if DOWNLOAD_SCREENSHOTS:
        download_screenshots(anime_list)
        round_scr = create_scr_round(anime_list[:])
        round_list.append(create_xml_round(round_scr, "image"))
    if DESC_ROUND:
        ...

    if GPT_ROUND:
        ...

    create_xml(round_list)

    transfer_audio()
    create_package()

    # print("Questions:")
    # for i in round.lines:
    #     for j in i.questions:
    #         print(j.answer)

    # for i in animes:
    #     print(i.hex_name)

    clear_trash()
    print("Done!")

if __name__=="__main__":
    ...
