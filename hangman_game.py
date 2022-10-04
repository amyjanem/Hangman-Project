# %%

import random


class Hangman:
    '''The classic Hangman game in which the user guesses letters until they correctly guess a word the computer has chosen or until they run out of lives.
    '''

    def __init__(self, word_list, num_lives = 5):
        '''This method initializes the following necessary attributes'''

        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''This method checks whether the user's guess is in the word chosen by the computer, and manages the number of unique letters left to guess as well as the number of lives left.'''
        
        guess = guess.lower()
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            print(f"You have {self.num_lives} lives left.")
            
            if self.word.count(guess) > 1:
                self.num_letters = self.num_letters - self.word.count(guess)
            else:
                self.num_letters -= 1
            
            for letter in range(0, len(self.word)):
                if self.word[letter] == guess:
                    self.word_guessed[letter] = guess
                    print(self.word_guessed)
                    print(f"You have {self.num_letters} letters left.\n")
            
            if self.num_letters == 1:
                print("You're almost there!\n")
        
        else:
            self.num_lives -= 1
            incorrect_response = ["Oh no!", "Sorry!", "Oh shucks!", "Incorrect!"]
            print(random.choice(incorrect_response), f"{guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.\n")
        
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        '''This method asks the user to input a letter they think will be in the word, and checks that the input is a unique single alphabetical character.'''

        while True:
            guess = input("Choose a letter")
            
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.\n")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!\n")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            break


def play_game():
    '''Calling this function will start the game of Hangman.'''

    word_list = ["pear", "orange", "strawberry", "apple", "banana"]
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_letters != 0:
            if game.num_lives > 0:
                game.ask_for_input()
            else:
                print("You lost!")
                break
        else:
            print("Congratulations. You won!")
            break       

play_game()