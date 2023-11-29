import random
words = ["man", "pall", "marwa"]
chance = 6
choice = random.choice(words)
word = [""]

for char in choice:
  word.append("_")

print(word)

while "_" in (word) and chance > 0:
  guess = input("Please Enter your guess: ").lower()
  if guess not in choice:
      chance -= 1

  for num in range(len(choice)):
    if guess == choice[num]:
      word[num] = guess

  print(word)   
  print(f"You have {chance} tries")
  
if chance> 0:
  print("""            ***********
        congratulation you won
            ***********""")
else:
  print("""You Lose
  +---+
  |   |
  o   |
 -|-  |
 / \  |
      |
=========""")


