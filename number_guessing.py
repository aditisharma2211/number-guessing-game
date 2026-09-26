import random

print("NUMBER GUESSING GAME")
number = random.randint(1,10)
#print(number) 


print("Guess the number- its between 1 to 10 ")
print("You only have three chances - use them wisely") 
  # logic for only three chance?

chances = 3
while (chances == 3 or chances == 2 or chances == 1 ):
  guess = int(input("Enter your guess: "))
  if number == guess:
    print("Congrats, You Won The Game!!!")
    break
  
  else:
    chances = chances - 1
    if chances == 0:
      print(f"You Are Now Out Of GUESSES. Please Restart The Game")
    else:
      print("Sorry, Please Try Again!")
      print(f"Now you are left with only {chances} chances")








    

