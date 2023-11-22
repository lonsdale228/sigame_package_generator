from pydub import AudioSegment
import os

def match_target_amplitude(sound, target_dBFS):
    """Normalize given audio segment to target dBFS."""
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Define the path to your folder containing the audio files
folder_path = fr'downloader\\Youtube\\'
target_dBFS = -20.0  # Target volume in dBFS, you can adjust this

def normalize_audio():
    for filename in os.listdir(folder_path):
        if filename.endswith('.m4a'):  # Change this to the appropriate file extension
            path = os.path.join(folder_path, filename)
            sound = AudioSegment.from_file(path)
            normalized_sound = match_target_amplitude(sound, target_dBFS)
            normalized_sound.export(path, format='m4a')  # Change format if needed
    print("Volume normalization complete.")