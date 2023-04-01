import os


def create_dirs():
    path=os.getcwd()
    os.chdir(path)
    if not os.path.exists("temp"):
        os.mkdir(r"temp")
        os.mkdir(r"temp\Audio")
        os.mkdir(r"temp\Video")
        os.mkdir(r"temp\Images")
