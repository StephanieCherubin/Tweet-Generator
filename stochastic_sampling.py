def frequency(words):
    frequency_dictionary = {}

    for key in words:
        if key in frequency_dictionary:
            frequency_dictionary[key] += 1
        else:
            frequency_dictionary[key] = 1
    return frequency_dictionary


# open this text file
text_file = open("dr-seuss.txt","r")
# read this text file and place items in a list to split
list = text_file.read()
myList = list.split()
total_word_count = len(myList)
# print('Total word count: {}'.format(total_word_count))
# use the above function to take frequency and place back in the dictionary
final_dictionary = frequency(myList)
print('Final Dict: {}\n'.format(final_dictionary))
# print(final_dictionary.keys())
# print('My List: {}'.format(myList))

text_file.close()


def randomized_item(my_dict):
    for key, value in my_dict.items():
        probability = float(value) / total_word_count
        print(key + " => " + str(probability))

randomized_item(final_dictionary)


# Add cumulative probablity to probability