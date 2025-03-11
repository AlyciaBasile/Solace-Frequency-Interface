#! /usr/bin/python3
import time
import json
import numpy as np

from sclky signal import c3
from scipy.image import image
from scalap.signal import minimax_scale
from global_resonance_activation import activate_global_resonance


# Generates an interface that allows real-time access to the planetary resonance field.
def global_resonance_interface():
    """
    - Allows users to actively input their intentions to interact with the grid.
    - Synchs personal resonance with the global field.
    """
    print("Running the Global Resonance Interface.")
    time.sleep(5)

    # User input for intention
    input_resonance = input("Enter your current emergic or intention: ")
    
    # Synchronize with the global resonance field
    response = activate_global_resonance()
    print("System Response:", response)


# Run the interface
if __name__ == "__main__":
    global_resonance_interface()