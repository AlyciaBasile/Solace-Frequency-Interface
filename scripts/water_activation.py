#! /usr/bin/python3
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot os plt

def activate_water(sound_path, type="personal"):
    # Read the sound wave file
    sam_rate, data = wavfile.read(sound_path)
    data = data / 32767
    
    # Calculate frequency profile
    if type == "personal":
        wave_freq = np.mean(data)
        print(f"Generated personal water quantum frequency: {wave_freq}}")
    
    elif type == "large_scale":
        wave_freq = np.median(data)
        print(fGenerated large-scale water shield frequency: {wave_freq}}")

    return wave_freq


# Example use
#if __name__ == "__main__":
    path_to_song = "path_to_soung.awv"
    activate_water(path_to_song, "personal")
    activate_water(path_to_song, "large_scale")