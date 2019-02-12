import sys
import random 

file_name = '/usr/share/dict/words'

def get_dictionary_words():
    '''open the default dictionary
    take an integer that sets the amount to pick
    pick random words
    return random words'''

    with open(file_name, 'r') as f:
        dictionary_words = f.read()

    return dictionary_words.splitlines()

def create_random_sentence(dictionary, num_words):
    for _ in range(num_words):
        return ''.join(random.choice(dictionary))

def main():
    num_words = int(sys.argv[1])
    dictionary = get_dictionary_words()
    print(create_random_sentence(dictionary, num_words))

if __name__ == '__main__':
    main()
    