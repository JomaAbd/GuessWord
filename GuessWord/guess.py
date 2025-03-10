import random
from enwords import words

def get_word():
    word = random.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "_"
    return display_letter
    
def play():
    word = get_word()
   	word_letters = set(word)

    user_letters = ''
    print(f"I thought {len(word)} lenght of word. Can you guess?")
    
    while len(word_letters) > 0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"You entered letters: {user_letters}")

        letter = input("Enter a letter: ").upper()
