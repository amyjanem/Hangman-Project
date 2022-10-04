# %%

import random


class Hangman:
    '''The classic Hangman game in which the user guesses letters until they correctly guess a word the computer has chosen or until they run out of lives.
    '''

    def __init__(self, word_list, num_lives = 5):
        '''This function initializes the following attributes:
        word_list: a list of words the computer will randomly select from
        word: the word randomly selected by the computer from words_list
        num_lives: the numbers of lives left (this starts at 5 by default)
        num_letters: the number of unique letters still left to be guessed by the user
        word_guessed: a list of the letters in the word, with '_' replacing unknown letters
        list_of_guesses: a list of guesses already tried  
        '''

        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''This function first converts the user's guess to lower case.
        It then checks whether the guess is in the word chosen by the computer, if it is, it replaces the '_' in the word_guessed with the actual letter, and decreases the amount of unique letters left to be guessed.
        It also checks if there are multiples of the same letter in the word. If so, it accordingly removes the amount of remaining unique letters left to be guessed.
        If the guessed letter is not in the word, the number of lives left is reduced by 1.
        Lastly, the guess is added to list_of_guesses to keep track of what has been guessed already.
        '''
        
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
        '''This function asks the user to input a letter they think will be in the word. 
        It makes sure the guess is an alphabetical letter, as one as one single character. If not, it reminds the user that it needs to be a single alphabetical character.
        It also checks if the user has already guessed the letter, and if so, reminds them to try a different letter.
        If the user inputs a unique guess correctly, the function then calls the check_guess function, and adds the guess to list_of_guesses.
        '''

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
    '''The play_game function sets the list of words to be chosen from by the computer. 
    It also sets the number of lives available to 5.
    The function uses a while True statement to ensure it continuously runs until told to break.
    Within this statement, the function checks if there are still unique letters to be guessed. If so, and the number of lives left are still more than 0, the ask_for_input function is called.
    Otherwise, if there are no lives left, the function tells the user they have lost. 
    After these checks, if the number of letters left equals to 0, the user is told that they have won. 
    '''

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