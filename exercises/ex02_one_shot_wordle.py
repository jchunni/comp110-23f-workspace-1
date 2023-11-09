"""EX02 One Shot Wordle!"""
__author__ = "730475774"
playing: bool = True
secret_word: str = "ghoul"

while playing:
    guess_word = input(f"What is your {len(secret_word)}-letter guess? ")
    while len(secret_word) != len(guess_word): 
        guess_word = input(f"That was not {len(secret_word)} letters! Try again:  ")
    else: 
        playing = False

WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"

result: str = ""
index: int = 0
while index < len(secret_word):
    if secret_word[index] == guess_word[index]: 
        result = result + GREEN_BOX
    else:
        letter_matched: bool = False
        checker_index = 0
        while checker_index < len(secret_word):
            if secret_word[checker_index] == guess_word[index] and checker_index != index: 
                result = result + YELLOW_BOX
                letter_matched = True
                playing = False
            checker_index = checker_index + 1
        if not letter_matched: 
            result = result + WHITE_BOX
    index = index + 1

if result == GREEN_BOX * len(secret_word): 
    print(result)
    print("Woo! You got it!")
else: 
    print(result)
    print("Not quite. Play again soon!")