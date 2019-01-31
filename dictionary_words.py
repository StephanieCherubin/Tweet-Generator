import random, sys

'''open the default dictionary
take an integer that sets the amount to pick
pick random words
return random words'''

def dictionary_words():
    file_name = '/usr/share/dict/words'
    with open(file_name) as file:
        defaultdict = file.read().split()
        # print(k = int(sys.argv[1]))
        random_word_s = random.sample(defaultdict, k = int(sys.argv[1]))
        str1 = ' '.join(random_word_s)

    print(str1)
    
dictionary_words()