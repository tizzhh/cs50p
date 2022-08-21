import sys

import random

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        while n <= 0:
            n = int(input("Level: "))
        break

rand = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        while guess <= 0:
            guess = int(input("Guess: "))
        while guess != rand:
            if guess < rand:
                print("Too small!")
                guess = int(input("Guess: "))
                while guess <= 0:
                    guess = int(input("Guess: "))
            elif guess > rand:
                print("Too large!")
                guess = int(input("Guess: "))
                while guess <= 0:
                    guess = int(input("Guess: "))
        print("Just right!")
        break