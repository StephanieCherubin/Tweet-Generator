import sys
import random 


def get_dictionary_words(file_name = '/usr/share/dict/words'):
    '''open the default dictionary'''
    
    with open(file_name, 'r') as f:
        dictionary_words = f.read()

    print(dictionary_words.splitlines())

# def create_random_sentence(dictionary, num_words):
#     '''take an integer that sets the amount to pick
#     pick random words
#     return random words'''
#     for _ in range(num_words):
#         return ''.join(random.choice(dictionary))

def main():
    # num_words = int(sys.argv[1])
    dictionary = get_dictionary_words()
    # print(create_random_sentence(dictionary, num_words))

if __name__ == '__main__':
    main()
    