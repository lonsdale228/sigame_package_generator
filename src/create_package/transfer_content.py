import glob
import os
import shutil

def get_files_with_extensions(directory, ext):
    abs_paths = []
    for extension in ext:
        rel_paths = glob.glob(os.path.join(directory, f'*.{extension}'))
        for path in rel_paths:
            abs_paths.append(os.path.abspath(path))
    return abs_paths

def transfer_audio():
    print("Transfering audio...")
    audio_path=fr"downloader\\Youtube\\"
    temp_path =fr"temp\\Audio\\"

    audio_extensions = ['mp3', 'm4a', 'wav', 'flac', 'ogg', 'aac', 'wma']
    audio_files=get_files_with_extensions(audio_path,audio_extensions)

    for file in audio_files:
        shutil.move(file,temp_path)
