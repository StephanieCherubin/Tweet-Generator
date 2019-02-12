import random, sys


def dictionary_words(num):
    '''open the default dictionary
    take an integer that sets the amount to pick
    pick random words
    return random words'''

    random_words = list()

    file_name = '/usr/share/dict/words'

    with open(file_name) as file:
        default_dict = file.read().split()
        while int(num) > len(random_words):
            random_number = random.randint(0,len(file_name)-1)
            randword = file_name[random_number]
            random_words.append(randword)

            final_string = ''.join(random_words)
            

    print(final_string)

if __name__ == "__main__":
    dictionary_words(input())
    