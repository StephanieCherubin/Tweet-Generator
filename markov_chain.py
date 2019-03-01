from dictogram import Dictogram

# corpus_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']


def markov_model(corpus_list):
    dictionary = {}
    for index in range(len(corpus_list) - 1):
        word = corpus_list[index]
        next_word = corpus_list[index + 1]
        if word not in dictionary:
            add_to_dict = Dictogram([next_word])
            dictionary[word] = add_to_dict
        else:
            dictionary[word].add_count(next_word)
    return dictionary

print(markov_model(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']))