import random

from histogram import frequency

with open("dr-seuss.txt","r") as f:
    lines = f.read().split(" ")
    total_word_count = len(lines)

    final_dictionary = frequency(lines)
    # print('Final Dictionary: {}\n'.format(final_dictionary))

def randomized_item(my_dict):
    # print('Percentage Count: ')
    for key, value in my_dict.items():
        probability = float(value) / total_word_count
        # print('{} => {}'.format(key, probability))

randomized_item(final_dictionary)


def probabilistic_word_sampler(final_dictionary):
    '''Sample words based on probablity. Run random function on list'''
    total = 0
    for key in final_dictionary:
        total += final_dictionary[key] 
        
    random_number = random.randrange(total)
    number_line_total = 0

    for key in final_dictionary:
        number_line_total += final_dictionary[key]

        if random_number < number_line_total:
            return key


def thousand_times():
    '''This function runs the above function 10,000 times. Then it creates a  histogram from resulting word'''

    thousand_dictionary = {}
    counter = 10000

    while counter > 0:

        random_word = probabilistic_word_sampler()

        if random_word in thousand_dictionary:
            thousand_dictionary[random_word] += 1

        else:
            thousand_dictionary[random_word] = 1
        counter -= 1
        
    return thousand_dictionary


if __name__ == '__main__':
    # print(probabilistic_word_sampler())
    print('\nStochastic Sampling: {}'.format(thousand_times()))   
