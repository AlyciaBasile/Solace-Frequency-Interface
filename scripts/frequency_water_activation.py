#! /usr/bin/python3
import numpy as np
from scipy.io import wavfile

def activate_water(song_path):
    # Read and process the sound file
    sam_rat, data = wavfile.read(song_path)
    data = data / 32767
    
    # Combine the signal with a function that simulates water activation
    wave_freq = np.mean(data)
    return wave_freq


# Use example
if __name__ == "__main__":
    song_file = "path_to_sound_file.wav"
    wave_signal = activate_water(song_file)
    print(f"Generated frequency for water activation: wave_signal")