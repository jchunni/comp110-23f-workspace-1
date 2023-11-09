"""Test my zip function."""
__author__ = "730475774"


from lessons.zip import zip


def test_len_dict_1() -> None:
    """When given 2 lists only 1 in length, will output a singular dict."""
    list1: list[str] = ['honey']
    list2: list[int] = [2]
    test_dict: zip(list1, list2) = {"honey": 2}
    assert zip(list1, list2) == test_dict


def test_empty_dict() -> None:
    """When used should return an empty dictionary."""
    assert zip([], []) == {}


def test_len_dict_3() -> None:
    """When given two lists that are 3 in length, returns a dictionary that is 3 in length."""
    list1: list[str] = ['honey', 'bear', 'sweet']
    list2: list[int] = [2, 4, 8]
    test_dict: zip(list1, list2) = {'honey': 2, "bear": 4, "sweet": 8}
    assert zip(list1, list2) == test_dict