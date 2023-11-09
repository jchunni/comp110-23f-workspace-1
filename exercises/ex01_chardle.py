"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730475774"

guess_word: str = input("Enter a 5-character word: ")
if (len(guess_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
guess_character: str = input("Enter a single character: ")
if (len(guess_character) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + guess_character + " in " + guess_word)

if (guess_character == guess_word[0]):
    print(guess_character + " found at index 0")
if (guess_character == guess_word[1]):
    print(guess_character + " found at index 1")
if (guess_character == guess_word[2]):
    print(guess_character + " found at index 2")
if (guess_character == guess_word[3]):
    print(guess_character + " found at index 3")
if (guess_character == guess_word[4]):
    print(guess_character + " found at index 4")
else:
    print()

count: int = sum(character == guess_character for character in guess_word) 
if (count == 0): 
    print("No instances of " + guess_character + " found in " + guess_word)
if (count == 1): 
    print("1 instance of " + guess_character + " found in " + guess_word)
if (count == 2):
    print("2 instances of " + guess_character + " found in " + guess_word)
if (count == 3):
    print("3 instances of " + guess_character + " found in " + guess_word)
if (count == 4): 
    print("4 instances of " + guess_character + " found in " + guess_word)
if (count == 5):
    print("5 instances of " + guess_character + " found in " + guess_word)
else:
    print()