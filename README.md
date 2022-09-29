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


## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
