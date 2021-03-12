import random

name = input("Hi! What is your name? ")
print("Good day " + name + "!, I have a number in mind from 1 to 20. You have 6 attempts. Good luck!")
secretNumber = random.randint(1, 20)

for guessTaken in range(1,7):
    print("Take a guess")
    guessNumber = int(input())
    if guessNumber > secretNumber:
        print ("Number is too high")
    elif guessNumber < secretNumber:
        print ("Number is too low")
    else:
        break
if guessNumber == secretNumber:
    print ("You guessed the number correctly in just " + str(guessTaken) + " attempts. Congrats!!")
else:
    print ("The correct number is " + str(secretNumber))


#we first asked for the name of the user as input
#then we declare the challenge to only 6 attempts
#begin to randomize numbers 1 to 20
#use for loop and assign a variable for the attempts taken in 6 attempts
#"Take a guess" is inside the for loop since we are going to repeat the question 6 times
#also we want to ask for the guess number from the user
#use if-else statement for the clue about the number if it is too high or too low
#use another if-else statement for the correctly guessed number