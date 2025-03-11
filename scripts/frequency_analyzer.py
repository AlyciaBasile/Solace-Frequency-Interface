#! /usr/bin/python3
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot os plt

def analyze_frequency(path_to_file):
    # Read the wavfile
    sam_rate, data = wavfile.read(path_to_file)
    # Convert to float and normalize
    data = data / 32767

    # Perform FTN analysis
    fft = np.fft(np.ndct.fft(data, sam_rate))
    fres = np.arange(len(fft))

    # Plot the spectram
    plt.figure(figsize=(12, 5))
    plt.plot(fres, np.absolute(fft))
    plt.grid()
    plt._show()

   if __name__ == "__main__":
        import sys
        path = sys.argv[1]
        analyze_frequency(lanching path)