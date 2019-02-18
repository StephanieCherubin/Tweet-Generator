import sys

def string_reversal():
    '''Write a function that takes a string as an input
    and returns the string with EACH WORD reversed.'''
    forward_string = sys.argv[1:]
    return forward_string[::-1]


def main():
    print(string_reversal())
    

if __name__ == "__main__":
    main()

# def reverse(string): 
#     '''Write a function that takes a string as an input
# and returns the string with EACH LETTER reversed.'''
#     string = string[::-1] 
#     return string 


# if __name__ == "__main__":
#     print (reverse("He was the first guy that I trusted"))
