# Hangman-Project

> This project consists of 3 milestones aimed to incrementally create the game Hangman. Each milestone introduces a step, from creating variables, checking whether guessed charaters are in the word, and creating the game class, which then is added all together in the final milestone where the user is able to play the game. 

## Milestone 1

- This milestone involved creating a program to return a random item from a list. Additionally, the program asks the user to enter a random letter of their choice. The code checks that the input is a single character, and if so, returns "Good guess!", and if not, returns "Oops! That is not a valid input"
  
```python
# %%
import random

# %%
word_list = ["apple", "banana", "orange", "strawberry", "watermelon"]

word = random.choice(word_list)

print(word)

# %%
guess = input("Choose a letter")

if len(guess)==1:
    print("Good guess!")
else: 
    print("Oops! That is not a valid input")
```


## Milestone 2

- In this milestone, code from the previous milestone was used to create functions, namely check_guess and ask_for_input.
- In the function ask_for_input, a while loop is used to ensure the code runs continuously. An if/else statement is then used to check whether the users input is a single character. 
- In the function check_guess, the users input is converted to lowercase using the .lower() method, and then an if/else statement is used to verify whether the users input is in the word that Python randomly selected.

```
import random


word_list = ["apple", "banana", "orange", "strawberry", "watermelon", "pineapple", "blueberry", "kiwi"]
        
word = random.choice(word_list)



def check_guess(guess):

    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        

def ask_for_input():
   
    while True:

        guess = input("Choose a letter")

        if len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)


ask_for_input()
```

## Milestone 3

- This milestone focused on creating a game class for the Hangman game. 
- The _ _ init _ _ method was used to initialise the attributes, such as word (word to be guessed), word_list (the list of words to be picked from), num_letters (number of unique letters in the word left to be guessed), num_lives (number of lives left, this starts at 5), list_of_guesses (a list of guesses already tried) and word_guessed (a list like the following ["_", "_", "_", "_"] depending on how many letters are in the randomly selected word, to be replaced with correct guesses)
- Two separate funtions were then defined, the check_guess and ask_for_input methods as previously described in Milestone 2, however in this instance, the functions also check that the input guess from the user is alphabetical as well as a single character. Additionally, an elif statement is used to check whether the user has already guessed a certain letter. After this, the function then adds the guess to a list of guesses (list_of_guesses).
- When a letter is correctly guessed by the user, a for-loop is used to cycle through each index position of the word, and replaces the '_' with the letter in the correct postion. This is done using the enumerate() function which adds a counter as the key of the enumerate object, in this case the word randomly chosen by Python.
- After the user guesses, a for-loop is used to reduce the number of letters remaining in the word to be guessed by 1.
- Within the check_guess method, if the user guesses a letter incorrectly, an else statement is used to reduce the number of lives the user has (num_lives) by 1. This incorrect guess is then added to a list to keep track of what has been guesses already (list_of_guesses).

```
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

            if guess.isaplha() == False or guess != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

ask_for_input()
```


## Final Milestone

- In this final milestone, all of the previous work gets put together. 
- A function called playgame() is created which will be called to play Hangman. 
- Within this function, a word_list is defined containing 5 fruits that Python will randomly select from. 
- An instance of the game is created with word_list and num_lives passed in as arguments.
- Within this, a while loop is used and set to True to check the following:
  - Firstly, if the num_lives left is equal to 0, in which case Python will tell the user they have lost
  - Secondly, if the num_letters is greater than 0, in which case the game will be continued by calling the ask_for_input method
  - And lastly, the code checks whether num_lives is not 0, AND if num_letters is not greater than zero, which means the user has won the game, thus the user is told that they have won.
- Following this the play_game function is called to begin the game

- Some personal enhancements that were added to the code inlude an encourangment message to be relayed to the user once they have one guess left. Additionally, the messages delivered for incorrect guesses were varied randomly, and the code now displays the visual of word as it is guessed similar to how you would write it out if playing on paper ie. ( _ p p _ e ) for apple

```
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
```


## Conclusions

- This project helped me understand the defining of functions, and how and when to call them. It also helped me with how to deal with errors, which in turn helped me understand the code better. 


