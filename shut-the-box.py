import random

def getRandomDiceRoll():
    return random.randint(1,7)

openList = [1,2,3,4,5,6,7,8,9,10,11,12]
closeList = ["_","_","_","_","_","_","_","_","_","_","_","_"]
diceOne = getRandomDiceRoll()
diceTwo = getRandomDiceRoll()

print("Your dice rolled a " + str(diceOne) + " and " + str(diceTwo))

def isRollValid():
    for x in openList: 
        if (diceOne == x or diceTwo == x):
            return True
        if (diceOne + diceTwo == x):
            return True
    return False

if (isRollValid()):
    userInput = input("(1) Use both numbers or (2) Use the sum of the numbers?")
else:
    print("There are no moves to make!")

if (userInput == '1'):
    if(openList.__contains__(diceOne)):
        print("The number is valid")
    if(openList.__contains__(diceTwo)):
        print("The number is valid")
elif(userInput == '2'):
    if(openList.__contains__(diceOne + diceTwo)):
        print("The sum is valid")
else:
    print("Invalid input")
