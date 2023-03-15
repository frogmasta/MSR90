# ==========================================
# Title:  example.py
# Author: Eric Roth
# Date:   March 14th, 2023
# ==========================================

import sys
import os
sys.path.append(os.getcwd() + "\\..\\src")

from msr90 import MSR90

def main():
    # Find the card reader
    reader = MSR90()
    reader.find_device()

    # Read a single card from the user
    print("Please swipe a card (time limit 10s): ", end=None)

    try:
        card = reader.read_card(timeout=10000)
    except TimeoutError:
        print("You never swiped your card...")
        return
    
    print(card)

if __name__ == "__main__":
    main()
