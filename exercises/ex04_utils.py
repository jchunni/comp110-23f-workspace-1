"""Utility Functions!"""
__author__ = "730475774"


def all(int_list: list[int], num: int) -> bool:
    """Returns True if all of the numbers in int_list are equal to the second argument and False otherwise."""
    for i in int_list:
        if i != num:
            return False
    return True if len(int_list) > 0 else False


def max(input: list[int]) -> int:
    """Given a list of integers, max should return the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max () arg is an empty list")
    current_max = input[0]
    for num in input:
        if num > current_max:
            current_max = num
    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of integer values, return True if every input at the same index is equal in both lists."""
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def main() -> None:
    """Implements all three functions."""
    print(all([1, 2, 3], 1))
    print(all([1, 1, 1], 2))
    print(all([1, 1, 1], 1))

    print(max([1, 3, 2]))
    print(max([100, 99, 98]))

    print(max([]))
    print(is_equal([1, 0, 1], [1, 0, 1]))
    print(is_equal([1, 1, 0], [1, 0, 1]))