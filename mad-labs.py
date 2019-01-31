'''Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, OR VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked into a NOUN and then VERB.
The program would find these occurences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
scrammed

The following text would be created:
"The silly panda walked to the chandelier and then scrammed.'''

color = input("Enter a color: ")
pluralNoun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are", color)
print(pluralNoun + " are blue")
print("I love", celebrity)