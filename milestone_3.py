# %%

import random

class Hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def check_guess(guess):
        
        guess = guess.lower()

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input():

        while True:
            guess = input("Choose a letter")

            if guess.isaplha() == False or guess != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses()
        








# %%
