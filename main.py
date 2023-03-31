import os
import downloader
from api_request.getAnimeInfo import getAnimeIds, getAnimeInfo
from create_package.create_package import create_package, clear_trash
from create_package.transfer_content import transfer_audio
from downloader.download import download_screenshots
from generate.generate_content import create_audio_line, create_round, create_xml_round, create_xml, create_scr_round

AUDIO_DURATION=30

if __name__=="__main__":
    #clear_trash()
    animes=getAnimeIds(5,"lonsdale651")
    ids=[]
    for i in animes:
        print(i.name)
        ids.append(i.id)
    print(ids)


    downloader.download(animes,10)
    curDir=os.getcwd()
    os.mkdir(f"{curDir}\\create_package\\temp")
    os.mkdir(f"{curDir}\\create_package\\temp\\Audio")
    os.mkdir(f"{curDir}\\create_package\\temp\\Images")
    os.mkdir(f"{curDir}\\create_package\\temp\\Video")
    #round=create_round(animes)
    #getScreenshot(animes)

    getAnimeInfo(animes)
    download_screenshots(animes)

    for i in animes:
        print(i.franchise)
        ids.append(i.id)
    print(ids)

    round=create_scr_round(animes)

    xml_round=create_xml_round(round,"image")
    xml_package=create_xml(xml_round)

    transfer_audio()
    create_package()
    clear_trash()



    # print("Questions:")
    # for i in round.lines:
    #     for j in i.questions:
    #         print(j.answer)


    # for i in animes:
    #     print(i.hex_name)
