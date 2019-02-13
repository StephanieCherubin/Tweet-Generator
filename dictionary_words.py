import random, sys


def dictionary_words(num):
    '''open the default dictionary
    take an integer that sets the amount to pick
    pick random words
    return random words'''

    file_name = '/usr/share/dict/words'

    with open(file_name) as file:
        words_list =[line.strip() for line in file] 
    
    output = ' '.join(random.sample(words_list, num)) + '.'

    print(output.capitalize())


if __name__ == "__main__":
    dictionary_words(9)

