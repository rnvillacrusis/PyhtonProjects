import random

def hangman():
    for guessTaken in range(1, 11):
        lst1 = ["project", "devops", "peace", "love", "champion", "powerful", "speed"]
        valid_letters = 'abcdefghijklmnopqrstuvwxyz'
        word = random.choice(lst1)

name = input("Hello there! What is your name?: ")
print("Hello" + name + ", let's save the slave from execution!")
print("Guess the word in ten attempts to save the slave!")
print("Take a guess! Enter a letter.")

# check if the letter is a valid character, set a string of valid characters for reference]
# if not valid, print "Enter a valid character from a to z"
# check if the letter is in the "word"
# print the position of the letter in that "word"
# if the letter is not in the "word", deduct attempts
# if the guess_word = word , print "You guessed the word".
# you can use an empty list for the guess_word
