import secrets


def set_anime_code(anime_list:list):
    for anime in anime_list:
        anime.hex_name=secrets.token_hex(16)




