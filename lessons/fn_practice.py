"""Example functions to learn definition and calling syntax"""



def my_max(num1: int, numr2: int) -> int:
    """Returns the maximum value out of 2 numbers"""
    if num1 >= num2:
        return num1
    else: #num1 < num2
        return num2

max_number: int = my_max(1,10)   
other_max_number: int = my_max(11,3)
print(other_max_number)