import random
import string



password =("")
print("Welcome to the password Generation!")
long_pass = int(input("Enter the total number of Characters in the password: "))
long_letter = int(input("Enter the number of Letters in the password: "))
long_num = int(input("Enter the number of Numbers in the password: "))
long_Symbols = int(input("Enter the number of Symbols in the password: "))

letters = random.choices(string.ascii_letters, k=(long_letter))
num = random.choices(string.digits, k=(long_num))
symbols = random.choices(string.punctuation, k=(long_Symbols))

test = letters+ num+ symbols
correct = random.shuffle(test)

if long_letter+long_num+long_Symbols == long_pass:
    for x in test:
      password += x
    print(f"Genarates Password: {password} ")
      


else:
    print("Invalid input. the sum of letters, numbers and symbols doesn't match the password")



