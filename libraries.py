import random

read = lambda filename: open(f"Libraries/{filename}.txt","r").read().split("\n")

class easy:
    def choose_word(self):
        return random.choice(read("easylib"))

class medium:
    def choose_word(self):
        return random.choice(read("mediumlib"))

class hard:
    def choose_word(self):
        return random.choice(read("hardlib"))
