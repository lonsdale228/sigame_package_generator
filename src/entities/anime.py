# class Anime:
#     def __init__(self, id=None, name=None, name_rus=None, hex_name=None, poster=None, anime_score=None, user_score=None,
#                  description=None, kind=None, franchise=None):
#         self.id = id
#         self.name = name
#         self.hex_name = hex_name
#         self.name_rus = name_rus
#         self.poster = poster
#         self.screenshot = []
#         self.anime_score = anime_score
#         self.user_score = user_score
#         self.description = description
#         self.kind = kind
#         self.franchise = franchise
#         self.genres = []


class Anime:
    id: int = None

    mal_id: int = None
    name: str = None

    name_rus: str = None
    kind: str = None
    score: float = None
    status: str = None
    episodes: int = None

    poster: str = None

    screenshots: list[str] = None
    scr_ext: str = None

    is_censored: bool = None

    genres: list[str] = None

    studios: list[dict] = None
    description: str = None

    hex_name: str = None
    user_score: str = None
    franchise: str = None

    characters: dict = None
