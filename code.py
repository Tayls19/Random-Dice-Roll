""" DICE ROLLING SIMULATOR: asks number of faces on die,
outputs a random number between 1 and number of faces,
and asks if user would like to reroll"""
from random import randint

dice = input("How many dice would you like to roll?")
    
while dice.isdigit() == False or int(dice) == 0:
  print("Please type a positive integer")
  dice = input("How many dice would you like to roll?")
if dice == 1:
  total_dice = ("1 die")

else:
  total_dice = (dice + " dice")

faces = input("How many faces on each die?")
while faces.isdigit() == False or int(faces) == 0:
  print("Please type a positive integer")
  faces = input("How many faces on each die?")
if faces == 0:
    print("Please type a positive integer")
    dice = input("How many dice would you like to roll?")
else:
    print(total_dice)
    print (faces + " faces")

faces = int(faces)
dice = int(dice)

roll = []
x = 1
while x <= dice:
  roll = roll + [randint(1, faces)]
  x += 1

tot = str(sum(roll))
roll = str(roll)

print ("Your roll: " + roll)
print ("Roll total: " + tot)

def checkstring(input):
    input = input.lower()
    if input == "yes" or input == "y":
<<<<<<< HEAD
        print("chocolate")
        return 1
    elif input == "no" or input =="n":
        print("labs")
        return 0
    else:
        print("are cute")
=======
>>>>>>> multipledie
        return 2
        
reroll = input("Would you like to roll again? Yes or No?")

while True:
    checkResult = checkstring(reroll)
    if checkResult == 0:
        break
    if checkResult == 1:
        roll = []
        x = 1
        while x <= dice:
            roll = roll + [randint(1, faces)]
            x += 1
        tot = str(sum(roll))
        roll = str(roll)
        print ("This is your NEW roll: " + roll)
        reroll = input ("Would you like to roll again? Yes, or No?")
    if checkResult == 2:
        print("Please type \"Yes\" or \"No\"")
        reroll = input ("Would you like to roll again? Yes, or No?")
print("Goodbye!")  
