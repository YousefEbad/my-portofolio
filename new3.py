import random
import string
words = ["office", "panda", "cabin", "ginger"]

letter = input("Please guess a letter: ")
correct = random.choice(words)

for x in correct:
    if x == letter:
        print("Right")
        
    else:
        print("Wrong")











