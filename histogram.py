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
    print('Histogram Dictionary: {}\n'.format(final_dictionary))

    list_of_tuples = []
    for key, value in final_dictionary.iteritems():
        list_of_tuples.append((key, value))
    print('List of Tuples: ' + str(list_of_tuples))

    list_of_lists = []
    for key, value in final_dictionary.iteritems():
        list_of_lists.append([key, value])
    print(list_of_lists)
    text_file.close()
    
histogram()


