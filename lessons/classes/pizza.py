"""Defining a Class!"""

from __future__ import annotations

#Think of a class definition as a "roadmap" for objects that belonf to the class you are defining the underlying structure every

class Pizza:
    """This is my class to represent pizza!"""

    #attributes
    #syntax <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        """Constructor"""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
        #by default returns self

    def price(self) -> float:
        """Method to compute price of pizza"""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost
    

    def add_topping(self, num_toppings: int):
        """Updates existing pizza order with num_toppings."""
        self.toppings += num_toppings

    def add_toppings_new_order(self, num_topping: int) -> Pizza:
        """Make new pizza order using existing info."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_topping, self.gluten_free)
        return new_pizza

