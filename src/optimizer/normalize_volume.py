from pydub import AudioSegment
import os



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
def match_target_amplitude(sound, target_dBFS):
    """Normalize given audio segment to target dBFS."""
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Define the path to your folder containing the audio files



def normalize_audio():
    folder_path = fr'downloader\\Youtube\\'
    target_dBFS = -10.0  # Target volume in dBFS, you can adjust this
    print(resource_path('ffmpeg/ffmpeg.exe'))
    AudioSegment.converter = resource_path('ffmpeg/ffmpeg.exe')
    AudioSegment.ffprobe = resource_path('ffmpeg/ffprobe.exe')
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp3'):  # Change this to the appropriate file extension
            path = os.path.join(folder_path, filename)
            sound = AudioSegment.from_file(path)
            normalized_sound = match_target_amplitude(sound, target_dBFS)
            normalized_sound.export(path, format='mp3')  # Change format if needed
    print("Volume normalization complete.")