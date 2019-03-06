from dictogram import Dictogram
from random import choice
import sys
from stochastic_sampling import probabilistic_word_sampler

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


def next_word(dictionary, word):
    # get the next word based on current word using the dictionary
    inner_dictionary = dictionary[word]  
    choice = probabilistic_word_sampler(inner_dictionary)
    return choice


# def nextWord(dictionary, word):
#     words = []
#     for index in dictionary[word].keys():
#         for _ in range(dictionary[word][index]):
#             words.append(index)
#     return choice(words)

# get the first word by indexing the array (sentence)

def generateSentences(parameter_list):
    pass

if __name__ == "__main__":
    print(markov_model(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']))
    return_dict = markov_model(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    print(next_word(return_dict, 'fish'))