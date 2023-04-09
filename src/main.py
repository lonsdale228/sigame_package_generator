import os
import downloader
from api_request.getAnimeInfo import getAnimeIds, getAnimeInfo, get_genres
from create_package.create_package import create_package, clear_trash
from create_package.transfer_content import transfer_audio
from downloader.download import download_screenshots, download_videos
from generate.generate_content import create_audio_line, create_round, create_xml_round, create_xml, create_scr_round
from src.api_request.setAnimeCode import set_anime_code
from src.generate import create_dirs
from src.optimizer.sort_anime import sort_by_genres

AUDIO_DURATION=30

#video\audio\screenshots
ANIME_COUNT=200

#max animes count from api
GET_ANIME_MAX=200

DOWNLOAD_SCREENSHOTS=True
DOWNLOAD_AUDIO=True


REMOVE_FRANCHISE_REPEAT=True

if __name__=="__main__":
    clear_trash()
    create_dirs()

    genres=get_genres()
    print(genres)
    anime_list=getAnimeIds(GET_ANIME_MAX,"lonsdale651")
    ids=[]
    for anime in anime_list:
        print(anime.name)
        ids.append(anime.id)
    print(ids)

    set_anime_code(anime_list)

    getAnimeInfo(anime_list,allow_duplicates=False)


    req_genres=['Drama']

    anime_list=sort_by_genres(anime_list,req_genres)

    download_videos(anime_list,AUDIO_DURATION,ANIME_COUNT)
    download_screenshots(anime_list)

    #round=create_round(anime_list)
    #getScreenshot(anime_list)

    #getAnimeInfo(anime_list)


    # for anime in anime_list:
    #     print(anime.franchise)
    #     ids.append(anime.id)
    # print(ids)

    round_scr=create_scr_round(anime_list[:])
    round_audio=create_round(anime_list[:])

    round_list=[]

    round_list.append(create_xml_round(round_scr,"image"))
    round_list.append(create_xml_round(round_audio,"audio"))

    xml_package=create_xml(round_list)

    transfer_audio()
    create_package()




    # print("Questions:")
    # for i in round.lines:
    #     for j in i.questions:
    #         print(j.answer)


    # for i in animes:
    #     print(i.hex_name)

    clear_trash()
