def frequency(words):
    frequency_dictionary = {}

    for key in words:
        if key in frequency_dictionary:
            frequency_dictionary[key] += 1
        else:
            frequency_dictionary[key] = 1
    return frequency_dictionary



def histogram():
    # open this text file
    text_file = open("twelve_years.txt","r")
    # read this text file and place items in a list to split
    list = text_file.read()
    myList = list.split()
    total_word_count = len(myList)
    print('Total word count: {}'.format(total_word_count))
    # use the above function to take frequency and place back in the dictionary
    final_dictionary = frequency(myList)
    # print('Final Dict: {}\n'.format(final_dictionary))
    # print(final_dictionary.keys())
    # print('My List: {}'.format(myList))
    text_file.close()
    return final_dictionary

my_dictionary = histogram()


def intermediate_histogram(my_dictionary):
    for key in my_dictionary:
        print('{} {}'.format(key, my_dictionary[key]))
intermediate_histogram(my_dictionary)
