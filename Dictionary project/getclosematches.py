from difflib import get_close_matches

data = ["small", "renzo", "dog","cat", "tommy", "polly"]
word = input("Please enter a word: ")
output = get_close_matches(word,data)[0]
print(output)


