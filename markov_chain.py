from dictogram import Dictogram
from stochastic_sampling import probabilistic_word_sampler
import random


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


def get_next_word(dictionary, word):
    # get the next word based on current word using the dictionary
    inner_dictionary = dictionary[word]  
    random_word_from_dictionary = probabilistic_word_sampler(inner_dictionary)
    return random_word_from_dictionary


def generate_sentences(dictionary):
    # get the first word by indexing the array (sentence)

    first_word = dictionary.keys()[0]
    # second_word = dictionary.keys()[1]
    second_word = get_next_word(dictionary, first_word)
    phrase = first_word + ' ' + second_word + ' '

    previous_word = second_word

    for word in range(0, random.randint(1,101)):
        new_word = get_next_word(dictionary, previous_word)
        # update previous word
        previous_word = new_word
        phrase += new_word + ' '
    return phrase


def second_order(corpus_list):
    second_order_dict = {}
    for index in range(len(corpus_list) - 2):
        word = corpus_list[index]
        next_word = corpus_list[index + 1]
        third_word = corpus_list[index + 2]

        second_order_tuple = (word, next_word)
        
        if second_order_tuple not in second_order_dict: 
            add_to_dictionary = Dictogram([third_word])
            second_order_dict[second_order_tuple] = add_to_dictionary
        else:
            second_order_dict[second_order_tuple].add_count(third_word)
    return second_order_dict
    

def generate_second_order_sentences(dictionary):
    # get the first word by indexing the array (sentence)
    phrase_list = []
    first_word = dictionary.keys()[0]
    # second_word = dictionary.keys()[1]
    second_word = get_next_word(dictionary, first_word)
    phrase.append(first_word)
    phrase.append(second_word)

    previous_word = second_word

    # loop while the last word is not stop token,
    # if it is the stop token, break loop
    for word in range(0, random.randint(1,101)):
        new_word = get_next_word(dictionary, previous_word)
        # update previous word
        previous_word = new_word
        phrase += new_word + ' '
    return ' '.join(phrase)


if __name__ == "__main__":
    # print(markov_model(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']))
    # return_dict = markov_model(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    # print(get_next_word(return_dict, 'fish'))
    # print(generate_sentences(return_dict))
    print(second_order(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'end']))