import os
import downloader
from api_request.getAnimeInfo import getAnimeIds, getAnimeInfo
from create_package.create_package import create_package, clear_trash
from create_package.transfer_content import transfer_audio
from downloader.download import download_screenshots, download_videos
from generate.generate_content import create_audio_line, create_round, create_xml_round, create_xml, create_scr_round
from src.api_request.setAnimeCode import set_anime_code
from src.generate import create_dirs

AUDIO_DURATION=30

#video\audio\screenshots
ANIME_COUNT=15

#max animes count from api
GET_ANIME_MAX=15

if __name__=="__main__":
    clear_trash()
    create_dirs()

    animes=getAnimeIds(GET_ANIME_MAX,"lonsdale651")
    ids=[]
    for i in animes:
        print(i.name)
        ids.append(i.id)
    print(ids)

    set_anime_code(animes)

    getAnimeInfo(animes)

    uniq_anim = {}
    for anime in animes:
        if anime.franchise==None:
            uniq_anim[f"{anime.name.replace(' ','')}"] = anime.id
        else:
            uniq_anim[f"{anime.franchise}"] = anime.id

    print(uniq_anim)

    download_videos(animes,AUDIO_DURATION,ANIME_COUNT)
    download_screenshots(animes)

    #round=create_round(animes)
    #getScreenshot(animes)

    #getAnimeInfo(animes)


    for i in animes:
        print(i.franchise)
        ids.append(i.id)
    print(ids)

    round=create_scr_round(animes)

    xml_round=create_xml_round(round,"image")
    xml_package=create_xml(xml_round)

    transfer_audio()
    create_package()




    # print("Questions:")
    # for i in round.lines:
    #     for j in i.questions:
    #         print(j.answer)


    # for i in animes:
    #     print(i.hex_name)

    clear_trash()
