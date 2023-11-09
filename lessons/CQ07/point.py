"""CQ07!!!"""
from __future__ import annotations
__author__ = "730475774"


class Point:
    """This is my class to represent Point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates!"""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Does not mutate."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point