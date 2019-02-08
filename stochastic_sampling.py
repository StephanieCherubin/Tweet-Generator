import random

from histogram import frequency

with open("dr-seuss.txt","r") as f:
        myList = f.read().split(" ")
        total_word_count = len(myList)

        final_dictionary = frequency(myList)
        print('Final Dict: {}\n'.format(final_dictionary))

def randomized_item(my_dict):
    for key, value in my_dict.items():
        probability = float(value) / total_word_count
        # print('{} => {}'.format(key, probability))

randomized_item(final_dictionary)

#Sample words based on probablity
# Run random function on list

def probabilistic_word_sampler():
    random_number = random.randrange(8)
#     print(random_number)
    return(myList[random_number])

print(probabilistic_word_sampler())


# Run above function 10000 times
# Create histogram from resulting word
# make a function that runs your probabilistic_word_sampler 10,000
def thousand_times():
        counter = 10000
        while counter > 0:
                random_word = probabilistic_word_sampler()
                print(myList[random_word])

                counter -= 1

# Make a new histogram that stores above function

thousand_times()