import random, sys

list = ["adam", "megan", "caroline", "alan", "milad", "dani"]

def rearrange(list):
    random_index = random.randrange(len(list))
    counter = 100
    while counter > 0:
        chosen_word = list.pop(random_index)
        list.append(chosen_word)
        counter -= 1
    result = ' '.join(list)
    print(result)


# def main(list):
#     rearrange(list)


# if __name__ == '__main__':
#     params = sys.argv[1:]
#     main(params)
rearrange(list)