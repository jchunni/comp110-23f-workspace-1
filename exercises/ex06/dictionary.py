"""Dictionary Functions!"""

__author__ = "730475774"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """When given a dictionary containing two strings, the function should return a dictionary that has inverted the placement of the strings."""
    invert_dict: dict[str, str] = {}
    for key in dictionary:
        if key in invert_dict[key]:
            raise KeyError("Key Error")
        else:
            invert_dict[dictionary[key]] = key
    return invert_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """When given a dictionary of names and favorite colors, it returns the str of color that appears most frequently."""
    color_count: dict[str, int] = {}
    for color in dictionary:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    return color in color_count


def count(list1: list[str]) -> dict[str, int]:
    """Given a list of strings, the function will return a dict of strings and ints where the key is the value of the list and the each valie is the count of the number of times the value appeared in the given list."""
    counter: dict[str, int] = {}
    for val in list1:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    return counter


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Given a list, the finction will create a dict where each key is a unique letter in the aphabet and each value is a list o the words that begin with that letter."""
    new_dict: dict[str, list[str]] = {}
    for word in list1:
        letter = word[0].lower()
        if letter not in new_dict:
            new_dict[letter] = []
        new_dict[letter].append(word)
    return new_dict


def update_attendance(log: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """Given a dictionary the funtion will mutate the dict with new attendance information given."""
    attendance_log: dict[str, list[str]] = {}
    if day in log:
        attendance_log[day].append(name)
    else:
        attendance_log[day] = [name]
    return attendance_log