from histogram import frequency


def histogram():
    with open('twelve_years.txt', 'r') as f:
        myList = f.read().split(" ")
        total_word_count = len(myList)
        final_dictionary = frequency(myList)
    return final_dictionary

my_dictionary = histogram()


def intermediate_histogram(my_dictionary):
    for key in my_dictionary:
        print('{} {}'.format(key, my_dictionary[key]))


if __name__ == "__main__":
   intermediate_histogram(my_dictionary) 