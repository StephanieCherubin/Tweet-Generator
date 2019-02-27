from random import choice
import sys

def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i + order]
        next_letter = text[i + order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model

def getNextCharacter(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)

def generateText(text, order, length):
    model = generateModel(text, order)
    currentFragment = text[0:order]
    output = ""
    for i in range(0, length-order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    print(output)

text = """I just got word today that the money is gonna be OK
and the weather oughta hold out through the weekend
Fall is settling in, the days are getting short again
and the morning is getting real nice for sleeping
Every time it gets colder I get another year older
I start looking for lines in the bathroom mirror
but when I lay down at night I swear I must have done something right
cause I am still so damn glad to be here"""
if __name__ == "__main__":
    generateText(text, int(sys.argv[1]), int(sys.argv[2]))