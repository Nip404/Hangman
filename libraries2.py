#libraries v2
import random

read = lambda filename: open("%s.txt" % filename,"r").read().split("\n")

class easy:
    def choose_word(self):
        return random.choice(read("easylib"))

class medium:
    def choose_word(self):
        return random.choice(read("mediumlib"))

class hard:
    def choose_word(self):
        return random.choice(read("hardlib"))
