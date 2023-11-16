"""Practice Writing Functions"""

def mimic(my_words: str) -> str: 
    """Given the string my_words, outputs the same string"""
    return my_words

mimic("Hello!")

print(mimic("Hello!"))

def mimic_letter(my_words: str, letter_idx: int) -> str: 
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words): 
        return "Index too high"
    #If we made it here, that means the letter_idx is valid, we can exit becuase it has a return
    return my_words[letter_idx]
