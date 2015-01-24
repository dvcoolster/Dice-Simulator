import random

MinValue = int(input("What is the minimum value of the dice?"))
MaxValue = int(input("What is the maximum value of the dice?"))

Roll = input("Would you like to roll the dice? (Yes or No)")
while Roll == ("Yes"):
    print ("Rolling the dices... The values are:")
    print (random.randint(MinValue,MaxValue))
    Roll = "No"

