from PyDictionary import PyDictionary

dictionary = PyDictionary(input("Please enter a word you want to define: "))

print(dictionary.printMeanings())
print(dictionary.getMeanings())
print(dictionary.getSynonyms())
