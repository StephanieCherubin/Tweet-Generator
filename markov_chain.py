from dictogram import Dictogram
from random import choice
import sys

# corpus_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']


def markov_model(corpus_list):
    dictionary = {}
    for index in range(len(corpus_list) - 1):
        word = corpus_list[index]
        next_word = corpus_list[index + 1]
        if word not in dictionary:
            add_to_dictionary = Dictogram([next_word])
            dictionary[word] = add_to_dictionary
        else:
            dictionary[word].add_count(next_word)
    return dictionary



def nextWord(dictionary, word):
    words = [ ]
    for index in dictionary[word].keys():
        for times in range(dictionary[word][index]):
            words.append(index)
    return choice(words)

if __name__ == "__main__":
    print(markov_model(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']))