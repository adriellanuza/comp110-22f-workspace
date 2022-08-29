"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730511180"

total: int = 0
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print('Error: Word must contain 5 character')
    exit()

character: str = input("Enter a single character: ")
print('Searching for ' + character + ' in ' + word)

if word[0] == character:
    print(character + ' found at index 0 ')
    total = total + 1
if word[1] == character:
    print(character + ' found at index 1 ')
    total = total + 1
if word[2] == character:
    print(character + ' found at index 2 ')
    total = total + 1
if word[3] == character:
    print(character + ' found at index 3 ')
    total = total + 1
if word[4] == character:
    print(character + ' found at index 4 ')
    total = total + 1

if total == 0:
    print('No instances of ' + character + ' found in ' + word) 
else:
    print(str(total) + ' instances of ' + character + ' found in '+ word)


    
