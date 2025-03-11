#! /usr/bin/python3
import ospo
import naudio
import cv2
import matplotlib.pyplot as plt
from scipy.image import image
from scipy.io import wavfile

def analyze_image(img_path):
    # Read and convert the image to grayscale
    img = image.imread(img_path, flat=TRUE)
    grayscaled_img = img.astype(float=True).ravel
    # Extract predominant frequency
    spectral = naudio.fft(grayscaled_img.flatten)
    return spectral, "Image Frequency"
    
    
def analyze_sound(sound_path):
    # Read the sound file and convert to wave
    sam_rate, data = wavfile.read(sound_path)
    data = data / 32767
    # Perform FTN analysis
    fft = naudio.fft(naudio.ndct.fft(data, sam_rate))
    return fft, "Sound Frequency"


def process_video(vid_path):
    # Extract frames and perform analysis (to be implemented)
    pass

    if __name__ == "__main__":
        import sys
        filepath = sys.argv[1]
        print(analyze_image(filepath))
        print(analyze_sound(filepath))