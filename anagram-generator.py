'''Write a function that determines if String A is an anagram of String B'''

'''
Examples:
(one, two) -> false
(bat, tab) -> true

Tougher Example:
(abba, baba) -> true
(aba, baba) -> false
(a ba, aa b) -> ???
(None, None) -?
'''

'''
Challenge your assumptions:
Are the words always going to be lowercase? What about upper and lower case?
What about spaces?
Are all letters unique?
'''

def frequency_count(word):
    frequency_dictionary = {}

    for key in word:
        if key in frequency_dictionary:
            frequency_dictionary[key] += 1
        else:
            frequency_dictionary[key] = 1
    return frequency_dictionary

def anagram_detector(string1, string2):
    frequency_string1 = get_char_count(word1)
    frequency_string2 = get_char_count(word2)

    for character in frequency_string2:
        if character in frequency_string1 and frequency_string1 > 0:
            frequency_string1[character] -= 1
        else:
            return False

    for character in frequency_string1:
        if frequency_string1[character] > 0:
            return False
