import json
from difflib import get_close_matches
data = json.load(open("data.json"))  #this will open and load the data.json file


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data(word.title())
    elif word.upper() in data:
        return data(word.upper())
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Do you mean %s instead?: " %get_close_matches(word, data.keys())[0])
        decide = input("Y or N: ")
        if decide == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "N":
            return ("Word entered is invalid")
        else:
            return ("You have entered an invalid answer")
    else:
        return ("Word not found")


word = input("Please enter any word you want to define: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)