class Generate():
    genres:list[int]=None

    num_of_getting:int=None
    num_of_total:int=None
    op_duration:int=None
    downloading_thread:int=None
    progress_bar:int=None
    nickname:str=""

    selected_genres:list[str] = None

    scr_round:bool=None
    op_round:bool=None
    desc_round:bool=None
    gpt_round:bool=None

    remove_duplicates:bool=None
    shuffle_lines:bool=None
    shuffle_questions:bool=None
    limit_theme:bool=None
    use_more_scr:bool=None

    ona:bool=None
    ova:bool=None
    specials:bool=None
    movie:bool=None

    rb_req_genres:bool=None
    rb_included_genres:bool=None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass