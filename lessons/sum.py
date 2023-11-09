"""Summing the elements of a list using different loops!"""
__author__ = "730475774"


def w_sum(vals: list[float]) -> float:
    """Sums with while loop."""
    idx: int = 0
    num: float = 0.0
    while idx < len(vals):
        num = sum(vals)
        return num
    idx += 1
    if idx < len(vals) is None:
        assert 0.0
    

def f_sum(vals: list[float]) -> float:
    """Sums with for statement."""
    num: float = 0.0
    for num in vals:
        num += vals[num]
    return num


def f_range_sum(vals: list[float]) -> float:
    """Sums with for statement and uses range."""
    total: float = 0.0
    for elem in range(0, len(vals)):
        total += vals[elem]
    return total