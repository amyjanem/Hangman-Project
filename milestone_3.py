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

    def check_guess(self, guess):
        
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        
        self.list_of_guesses.append(guess)

    def ask_for_input(self):

        while True:
            guess = input("Choose a letter")

            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game():
    word_list = ["watermelon", "orange", "strawberry", "apple", "banana"]
    game = Hangman(word_list, num_lives = 5)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_lives > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters < 1:
            print("Congratulations. You won!")
            break
        else:
            break
            

play_game()

# %%
