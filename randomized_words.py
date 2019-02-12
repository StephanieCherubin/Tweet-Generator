
import random

file_name = '/usr/share/dict/words'

def load_words():
    # with open('words.txt', 'r') as f:
    with open(file_name, 'r') as f:
        # get each string separated by a space
        # put each string in an array
        f_contents = f.readlines() # list of each line of the file
        # Not from file:
        # f_contents = ["zythem", "Zythia", "zythum", "Zyzomys", "Zyzzogeton"]
    return f_contents


def get_rand_int_of_words(f_contents):
    words_list = []
    # f_contents = load_words()
    # print(f'Words in the file: {f_contents}') # Check output
    # pick a number by random that will be the number of words you want to get from the words file
    numOfWords = random.randrange(2, len(f_contents))
    # print(f"Random number of words: {numOfWords}") # Check output
    for wordIndex in range(0, numOfWords):
        word = f_contents[wordIndex]
        # print(f'The word: {word}') # Check output
        words_list.append(word)
    return words_list
        # f_word = f.readline()


if __name__ == '__main__':
    load_words = load_words()
    # print(f"Words from file: {load_words}")
    get_words_list = get_rand_int_of_words(load_words)
    # print(f"Random amount of words: {get_words_list}")
    put_in_sentence = put_in_sentence(get_words_list)
    # print(put_in_sentence)