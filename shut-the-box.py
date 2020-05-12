import random

def getRandomDiceRoll():
    return random.randint(1,7)

openList = [1,2,3,4,5,6,7,8,9,10,11,12]
closeList = ["_","_","_","_","_","_","_","_","_","_","_","_"]
diceOne = getRandomDiceRoll()
diceTwo = getRandomDiceRoll()

print("Your dice rolled a " + str(diceOne) + " and " + str(diceTwo))

