import random
words=["good", "bad", "ugly"]

choice = random.choice(words)
print(choice)
space=[]
for x in choice:
    space.append("_")

print(space)

guess = input("Please guess a leter: ").lower()
while("_") in space:
    guess = input("Please guess a leter: ").lower()
    for pos in range(len(choice)):
        if guess == choice[pos]:
            space[pos] = (guess)
           
    print(space)
            
            
        
            
print("You Win")

        
            
        
        





