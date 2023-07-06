#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game."""
print("Guess the music genre!")
    
genre =   [
        "kpop",
        "rock",
        "jpop",
        "electronic music",
        "jazz",
        "hip hop",
        "classical music"]
    
x = random.choice(genre)
guess = None

while x != guess:
    
    guess = str(input("pick a music genre :"))
    
    if x == guess:
        print("Congratulations!")
    else :
        print("try again!")
        
main()