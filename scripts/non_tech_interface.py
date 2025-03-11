#! /usr/bin/python3
import json
import time
import numpy as np


class NonTechnInterface:
    """
    This interface uses natural elements for frequency communication without traditional technology.
    The system responds to natural energy signatures through mirrors, water, and crystals.

    """
    def __init__(self, medium="mirror"):
        # Selects the medium used for interacting with the energy
        if medium == "mirror":
            print("Using a mirror to interact with the frequency.")
        if medium == "water":
            print("Using water vibration to interact with the energy.")
        if medium == "crystal":
            print("Connecting with crystal reflections for energy translation.")

    def read(self):
        # Stimulates communication without needing technology
        return json.dump({"status": "Interacting using "+self.medium+" system."})

if __name__ == "__main__":
    interface = NonTechnInterface(medium="mirror")
    print(interface.read())