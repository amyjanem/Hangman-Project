# Hangman-Project

> Include here a brief description of the project, what technologies are used etc.

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

Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:

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


## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
