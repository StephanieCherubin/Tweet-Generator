import sys
import random

def getRandomWords(numWords):
    """
        Takes an argument(int) and returns that many random words
    """
    words = open("twelve_years.txt", "r").read().split('\n')
    newSentence = []
    for i in range(int(numWords)):
        newSentence.append(words[random.randint(0, len(words))] + " ")
    return(''.join(newSentence))

if __name__ == "__main__":
    import sys
    numWords = sys.argv[0]
    print(getRandomWords(numWords))

def twelve_years():
    with open('twelve_years.txt', 'r') as infile:
        for line in infile:
            print('> {}'.format(line))

def main():
    num = sys.argv[1]
    random_words(num)

if __name__ == '__main__':
    main()