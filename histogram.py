with open('twelve_years.txt', 'r') as f:
    lines = f.read().split(" ")

def frequency(words):
    frequency_dictionary = {}

    for key in words:
        
        if key in frequency_dictionary:
            frequency_dictionary[key] += 1
        else:
            frequency_dictionary[key] = 1

    return frequency_dictionary


def dictogram():
    final_dictionary = frequency(lines)
    return 'Histogram Dictionary: {}\n'.format(final_dictionary)


def list_of_tuples():
    # Tuples are immutable. It cannot be changed once created.
    list_of_tuples = []

    for word in lines:
        found = False 

        for inner_tuple in list_of_tuples:
            if word == inner_tuple[0]:
                count = inner_tuple[1] + 1
                list_of_tuples.remove(inner_tuple)
                list_of_tuples.append((word, count))
                found = True
        
        if not found:
            list_of_tuples.append((word, 1))
    
    return 'Tuplegram: {}\n'.format(list_of_tuples)
    

def list_of_lists():
    list_of_lists = []
    for word in lines:
        found = False 

        for inner_list in list_of_lists:

            if word == inner_list[0]:
                count = inner_list[1] + 1
                list_of_lists.remove(inner_list)
                list_of_lists.append((word, count))
                found = True
        
        if not found:
            list_of_lists.append((word, 1))
    
    return 'Listogram: {}\n'.format(list_of_lists)



if __name__ == "__main__":
    # print(frequency(lines))
    print(dictogram())
    print(list_of_tuples())
    print(list_of_lists())

