import asyncio
import pickle
import random
from api_request.getAnimeInfo import getAnimeIds, get_anime_info, remove_duplicates
from create_package.create_package import create_package, clear_trash
from create_package.transfer_content import transfer_audio
from downloader.download import download_screenshots, download_videos
from generate.generate_content import create_rounds, create_xml, create_xml_rounds
from src.api_request.setAnimeCode import set_anime_code
from src.entities.rounds import Round
from src.generate import create_dirs
from entities.generate import Generate
from src.optimizer.compress_images import compress_images
from src.optimizer.normalize_volume import normalize_audio
from src.optimizer.sort_anime import sort_by_genres, force_sort_by_genres, sort_by_kind

from entities.anime import Anime


def resource_path(relative_path):
    import os
    import sys
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main(settings: Generate, win):
    AUDIO_DURATION: int = settings.op_duration
    ANIME_COUNT: int = settings.num_of_total
    GET_ANIME_MAX: int = settings.num_of_getting

    # rounds
    DOWNLOAD_SCREENSHOTS: bool = settings.scr_round
    DOWNLOAD_AUDIO: bool = settings.op_round
    DESC_ROUND: bool = settings.desc_round
    GPT_ROUND: bool = settings.gpt_round

    # creation modifier
    REMOVE_FRANCHISE_REPEAT: bool = settings.remove_duplicates
    SHUFFLE_LINES: bool = settings.shuffle_lines
    SHUFFLE_QUESTIONS: bool = settings.shuffle_questions


    NICKNAME: str = settings.nickname

    # kind sort
    ONA_RB: bool = settings.ona
    OVA_RB: bool = settings.ova
    MOVIE_RB: bool = settings.movie
    SPECIAL_RB: bool = settings.specials

    IMAGE_QUALITY: int = settings.image_compress_percent
    AUDIO_QUALITY: int = settings.audio_compress_bitrate
    COMPRESS_AFTER: int = settings.compress_after

    DONT_USE_GENRES: bool = settings.dont_use_genres

    THREAD_NUM = settings.downloading_thread

    win.set_progress(value=0)

    clear_trash()
    create_dirs()

    file = open(resource_path('15000_animes.txt'), 'rb')
    anime_dump = pickle.load(file)
    file.close()

    anime_list = getAnimeIds(GET_ANIME_MAX, NICKNAME)

    ids = []
    for anime in anime_list:
        ids.append(anime.id)

    getting_list = []

    for get in getting_list:
        print(get.name)
    for anime in anime_list:
        if anime.id not in anime_dump:
            getting_list.append(anime)

    print(*[i.name for i in getting_list], sep='***')
    get_anime_info(getting_list)

    for i in range(len(anime_list)):
        try:
            anime_list[i] = anime_dump[anime_list[i].id]
        except Exception as e:
            print('error: ', e)

    set_anime_code(anime_list)

    anime_list = anime_list + getting_list

    if REMOVE_FRANCHISE_REPEAT:
        anime_list: list[Anime] = remove_duplicates(anime_list)
    random.shuffle(anime_list)

    # kind sort
    sort_by_kind(anime_list, ONA_RB, OVA_RB, SPECIAL_RB, MOVIE_RB)

    # genre sort
    if not DONT_USE_GENRES:
        req_genres = settings.selected_genres
        if settings.rb_req_genres:
            anime_list = sort_by_genres(anime_list, req_genres)
        else:
            anime_list = force_sort_by_genres(anime_list, req_genres)

    # limit total anime count
    anime_list: list[Anime] = anime_list[:ANIME_COUNT]

    round_list: list[Round] = []

    if DOWNLOAD_AUDIO:
        download_videos(anime_list, AUDIO_DURATION, THREAD_NUM ,quality=AUDIO_QUALITY)
        # normalize_audio()
        rounds_audio = create_rounds(anime_list[:], line_limit=10, per_line_limit=15, round_type='voice')
        round_list = round_list + rounds_audio

    if DOWNLOAD_SCREENSHOTS:
        asyncio.run(download_screenshots(anime_list))
        if IMAGE_QUALITY!=100:
            compress_images(IMAGE_QUALITY,COMPRESS_AFTER)
        rounds_scr = create_rounds(anime_list[:], line_limit=10, per_line_limit=15, round_type='image')
        round_list = round_list + rounds_scr

    if DESC_ROUND:
        ...

    if GPT_ROUND:
        ...

    round_list = create_xml_rounds(round_list, shuffle_lines=SHUFFLE_LINES, shuffle_questions=SHUFFLE_QUESTIONS)

    repeat_test = []
    repeated = []
    for a in anime_list:
        if a.franchise in repeat_test:
            repeated.append(a)
        repeat_test.append(a.franchise)

    print("Anime repeates: ", len(repeated))

    create_xml(round_list, NICKNAME)

    transfer_audio()
    create_package()

    clear_trash()
    print("Done!")


if __name__ == "__main__":
    ...
