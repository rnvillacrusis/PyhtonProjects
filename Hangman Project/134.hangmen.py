import random
def hangman():

    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'   # this will be the valid letters
    turns = 10
    guessmade = ''   # this will contain the letter from the user

    while len(word) > 0:  # this will ensure that the word exist since length==0 means empty string
        main = ""   # this will be the container of the correct letters guessed by the user until it is complete
        missed = 0

        for letter in word:   # this will check if letter in guessmade is also in the word
            if letter in guessmade:  # if letter is in the word, it will print the guessed letters in the word for example "_e__e_" in the word secret
                main = main + letter    # then it will add that letter to main
            else:
                main = main + "_" + " "  # first output of main is a set of underscores with corresponding number of letter in that random word
        if main == word:
            print("You guessed the correct word:", main.upper())
            print("You win!")
            break                   # no break means it will just continue the program even you already guessed the correct word


        print("Guess the word:", main) #see line 17, it will first display underscores since no input has been made, until a guess is correct
        guess = input()

        if guess in validLetters:   # this will check if the character is a valid input
            guessmade = guessmade + guess  # if the character is valid, it will add the letter to the empty string guessmade.
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("Enter your name")
print("Welcome" , name )
print("-------------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()
