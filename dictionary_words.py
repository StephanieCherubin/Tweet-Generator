import random


def dictionary_words(num):
    '''open the default dictionary
    take an integer that sets the amount to pick
    pick random words
    return random words'''

    file_name = 'twelve_years.txt'

    with open(file_name) as file:
        words_list = file.read().split(" ")
    
    output = ' '.join(random.sample(words_list, num)) + '.'

    return output.capitalize()


if __name__ == "__main__":
    dictionary_words(9)

