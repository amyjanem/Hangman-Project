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

> Insert an image/screenshot of what you have built so far here.

## Milestone 2

- Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:

```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
