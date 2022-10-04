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


# %%
