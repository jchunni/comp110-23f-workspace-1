"""Dict Unite Tests."""
__author__ = "730475774"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_empty_invert() -> None:
    """When given no inputs, will return an empty dictionary."""
    assert invert([]) == {}


def test_invert_dict1() -> None:
    """When given a dictionary with a length of 1, will return inverted dictionary with length of 1."""
    input_dict: dict[str, str] = {"honey": "sweet"}
    test_dict = {"sweet": "honey"}
    assert invert(input_dict) == test_dict


def test_invert_dict3() -> None:
    """When given a dictionary with a length of 3, will return inverted dictionary with length of 3."""
    input_dict: dict[str, str] = {"honey": "sweet", "ellie": "oppie", "lindsay": "cat"}
    test_dict = {"sweet": "honey", "oppie": "ellie", "cat": "lindsay"}
    assert invert(input_dict) == test_dict


def test_empty_color() -> None:
    """When given an empty dictionary, will return empty string."""
    assert favorite_color([]) == ""


def test_len_color1() -> None:
    """When given a dictionary that has the length of 1, will return the color seen."""
    input_dict: dict[str, str] = {"ellie": "blue"}
    expected: favorite_color(input_dict) = "blue"
    assert favorite_color(input_dict) == expected


def test_len_color4() -> None:
    """When given a dictionary with a length of 3, will return the color seen most."""
    input_dict: dict[str, str] = {"ellie": "blue", "lindsay": "pink", "olivia": "pink", "jillian": "blue"}
    expected: favorite_color(input_dict) = "blue"
    assert favorite_color(input_dict) == expected


def test_empty_count() -> None:
    """Given an empty list, returns an empty dictionary."""
    assert count([]) == {}


def test_count_1() -> None:
    """When given a list of strings, will count how many times that value appears in list and return dict."""
    input_list: list[str] = ["ellie", "oppie", "lindsay"]
    expected_result: dict[str, int] = {"ellie": 1, "oppie": 1, "lindsay": 1}
    assert count(input_list) == expected_result


def test_count_2() -> None:
    """When given a list of str, will count how many times that value appears in the list and will return a dictionary."""
    input_list: list[str] = ["ellie", "oppie", "ellie"]
    result: dict[str, int] = {"ellie": 2, "oppie": 1}
    assert count(input_list) == result


def test_empty_alphabetizer() -> None:
    """When given an empty list, will return an empty dictionary."""
    assert alphabetizer([]) == {}


def test_alphabetizer_2() -> None:
    """When given a list with a length of 2, will return a dict where each key is a letter of the alphabet and each value is a list of words that begin with that letter."""
    input_list: list[str] = ["apple", "banana"]
    result: dict[str, list[str]] = {"a": ["apple"], "b": ["banana"]}
    assert alphabetizer(input_list) == result


def test_alphabetizer_3() -> None:
    """When given a list with a length of 3, will return a dict where each key is a letter of the alphabet and each value is the list of words that begin with that letter (has more than one in list)."""
    input_list: list[str] = ["apple", "banana", "boy"]
    result: dict[str, list[str]] = {"a": ["apple"], "b": ["banana", "boy"]}
    assert alphabetizer(input_list) == result
    

def test_empty_attendance() -> None:
    """When given an empty dict, and no str, will return an empty dict."""
    assert update_attendance([], [], "", "") == {}


def test_update_attendance1() -> None:
    """When given a dict of days and students and then a new day and student, will mutate and return dict of new attendance."""
    input_dict: dict[str, list[str]] = {"monday": ["oppie"], "tuesday": ["ellie"]}
    day: str = "wednesday"
    name: str = "jillian"
    assert update_attendance(input_dict, day, name) == {"monday": ["oppie"], "tuesday": ["ellie"], "wednesday": ["jillian"]}


def test_update_attendance2() -> None:
    """When given a dict of days and students and then str of day and name, will mutate and return dict of new attendance."""
    input_dict: dict[str, list[str]] = {"monday": ["oppie"], "tuesday": ["ellie"]}
    day: str = "monday"
    name: str = "jillian"
    assert update_attendance(input_dict, day, name) == {"monday": ["oppie", "jillian"], "tuesday": ["ellie"]}