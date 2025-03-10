import random
from enwords import words

def get_word():
    word = random.choice(words)
    return word.upper()