# This program will let the user guess the number
import random

print("Hello, What is your name?")
name = input()

print("Well," + name + ",I am thinking of a number from 1 to 20")
secretNumber = random.randint(1, 20)


for guessTaken in range(1, 7):
    print("Take a guess.")
    number = int(input())
    if number > secretNumber:
        print("Too high.")
    elif number < secretNumber:
        print("Too low.")
    else:
        break
if number == secretNumber:
    print("Great," + name + ",you have guess the correct number in " + str(guessTaken) + " attempts!!")
else:
    print("Nope. The number is " + str(secretNumber) + ".")
