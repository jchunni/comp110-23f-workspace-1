"""Combinging two lists into a dictionary."""
__author__ = "730475774"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Function should produce a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    if len(list1) == 0 or len(list2) == 0:
        return {}
    if len(list1) != len(list2):
        return {}
    dictionary = {}
    for i in range(len(list1)):
        dictionary[list1[i]] = list2[i]
    return dictionary
    

