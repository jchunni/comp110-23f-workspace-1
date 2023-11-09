"""EX03 - Structured Wordle!"""
__author__ = "730475774"
WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"


def contains_char(haystack: str, needle: str) -> bool:
    """When given 2 strings with the first one being of any length and the second one being a single character,the function will return True if the character of the 2nd variable is found at any index of the first string."""
    assert len(needle) == 1
    idx: int = 0
    includes_word: bool = False
    while len(haystack) > idx: 
        if haystack[idx] == needle:
            includes_word = True
            idx += 1
        else:
            idx += 1
    return includes_word


def emojified(guess: str, secret_word: str) -> str:
    """When given two strings of equal length, the first being a guess and the second being a secret, it will return a color emoji on how it matches up."""
    assert len(guess) == len(secret_word)
    result: str = ""
    idx: int = 0
    while idx < len(guess):
        if contains_char(secret_word, guess[idx]) is True and secret_word[idx] == guess[idx]:
            result = result + GREEN_BOX
        elif contains_char(secret_word, guess[idx]) is True and secret_word[idx] != guess[idx]:
            result = result + YELLOW_BOX
        elif contains_char(secret_word, guess[idx]) is False:
            result = result + WHITE_BOX
        idx = idx + 1
    return result


def input_guess(expected_length: int) -> str:
    """This will prompt users for a guess and to see if the guess is the expected length, if it isn't it will continue to promt."""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """This is the main part of the game."""
    playing = True
    secret_word: str = "codes"
    number_turns = 1
    while number_turns <= (len(secret_word) + 1) and playing is True:
        print(f"=== Turn {number_turns}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {number_turns}/6 turns!")
            playing = False
        else:
            number_turns += 1
        if number_turns > 6:
            print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()