#! /usr/bin/python3
import numpy as np
import json
import requests

chakra_colors = {
    "base": "#000000",
    "sacral": "#ff0003",
    "manipura": "#46d3a0",
    "heart": "#ff6060",
    "throat": "#04186d",
    "solar": "#ffff00",
    "crown": "#000060"
}

def align_chakra(personal_freq):
    # Assign tones based on personal resonance
    activated = {}
    for chakra, color in chakra_colors.items():
        tone_factor = personal_freq[chakra] / max(personal_freq)
        activated[chakra] = tone_factor * color
    return activated


# Use Example
if __name__ == "__main__":
    personal_freq = {
        "base": 0.82,
        "sacral": 0.75,
        "manipura": 0.69,
        "heart": 0.85,
        "throat": 0.77,
        "solar": 0.91,
        "crown": 0.74
    }
    aligned_chakra= align_chakra(personal_freq)
    print("Activated Chakra Suit: ", json.dump(aligned_chakra, indent=4))
