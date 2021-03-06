import random, sys

def rearrange():
    '''Takes user input words from terminal and rearranges them while shuffling 1000 times.'''
    words_from_terminal = sys.argv[1:]
    counter = 1000
    while counter > 0:
        random_index = random.randrange(len(words_from_terminal))
        chosen_word = words_from_terminal.pop(random_index)
        words_from_terminal.append(chosen_word)
        counter -= 1
    result = ' '.join(words_from_terminal)
    print(result)

if __name__ == "__main__":
    rearrange()
