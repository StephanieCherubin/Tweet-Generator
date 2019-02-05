import random, sys


def rearrange():
    words_from_terminal = sys.argv[1:]
    counter = 100
    while counter > 0:
        random_index = random.randrange(len(words_from_terminal))
        chosen_word = words_from_terminal.pop(random_index)
        words_from_terminal.append(chosen_word)
        counter -= 1
    result = ' '.join(words_from_terminal)
    print(result)

if __name__ == "__main__":
    rearrange()