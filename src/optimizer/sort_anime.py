def force_sort_by_genres(anime_list: list, genres: list):
    sorted_list = []
    for anime in anime_list:
        try:
            if all(genre in anime.genres for genre in genres) and anime.genres and anime not in sorted_list:
                sorted_list.append(anime)
        except Exception as e:
            print(e)
    return sorted_list


def sort_by_genres(anime_list: list, genres: list):
    sorted_list = []
    for anime in anime_list:
        try:
            for genre in genres:
                if genre in anime.genres:
                    sorted_list.append(anime)
                    break
        except Exception as e:
            print(e)
    return sorted_list


def sort_by_kind(anime_list: list, ONA_RB :bool, OVA_RB :bool, SPECIAL_RB :bool, MOVIE_RB :bool):
    for_remove = []
    if not ONA_RB:
        for i in range(len(anime_list)):
            if anime_list[i].kind in ['ona', 'tv', 'tv_13', 'tv_24', 'tv_48']:
                for_remove.append(anime_list[i])
    if not OVA_RB:
        for i in range(len(anime_list)):
            if anime_list[i].kind in ['ova']:
                for_remove.append(anime_list[i])
    if not SPECIAL_RB:
        for i in range(len(anime_list)):
            if anime_list[i].kind in ['special']:
                for_remove.append(anime_list[i])
    if not MOVIE_RB:
        for i in range(len(anime_list)):
            if anime_list[i].kind in ['movie']:
                for_remove.append(anime_list[i])

    for i in for_remove:
        anime_list.remove(i)