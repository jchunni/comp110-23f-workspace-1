"""Quiz 2 practice."""
__author__ = "730475774"


def short_words(input_list: list[str]) -> list[str]:
    """Short words function."""
    new_list: list[str] = []
    i: int = 1
    while i < len(input_list):
        if len(input_list[i]) > 5:
            return (f"{input_list[i]} is too long!")
        else:
            new_list += input_list[i]
    return new_list


def shortwords(input_list: list[str]) -> list[str]:
    """Finds the short words."""
    new_list: list[str] = []
    for word in input_list:
        if len(word) < 5:
            new_list.append(word)
        else:
            print(f"{word} is too long!")
    return new_list