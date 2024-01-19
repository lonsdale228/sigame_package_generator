import re

from src.entities.anime import Anime


def clear_description(anime_list: list[Anime]):
    for i, anime in enumerate(anime_list):
        desc = anime.description
        if desc:
            text_without_brackets = re.sub(r'\[.*?\]', '', desc)
            modified_text = re.sub(r'\b[А-ЯЁ][а-яё]*\b', '...', text_without_brackets)
            anime.description = modified_text
