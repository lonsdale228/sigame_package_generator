# def sort_by_genres(anime_list:list,genres:list):
#     sorted_list=[]
#     for anime in anime_list:
#         try:
#             if all(genre in anime.genres for genre in genres) and anime.genres:
#                 sorted_list.append(anime)
#         except Exception as e:
#             print(e)
#     return sorted_list

def sort_by_genres(anime_list:list,genres:list):
    sorted_list=[]
    for anime in anime_list:
        try:
            for genre in genres:
                if genre in anime.genres:
                    sorted_list.append(anime)
                    break
        except Exception as e:
            print(e)
    return sorted_list