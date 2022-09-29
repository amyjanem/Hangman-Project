# %%

import random

class Hangman:

    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives

    num_lives = 5

    def word(self, word_list):
        return random.choice(word_list)

    def word_guessed(self):
        



# %%
