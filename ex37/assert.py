"""
Try 'assert' keyword
"""


def add(a, b):
    """ add two numbers"""
    # return a + b + b
    return a + b


# Test the add function with assert statements

# assert condition, message
# if condition is False,
# the program will raise an AssertionError with the specified message.

assert add(2, 3) == 5, "add(2, 3) should be equal to 5"
assert add(-1, 5) == 4, "add(-1, 5) should be equal to 4"
assert add(0, 0) == 0, "add(0, 0) should be equal to 0"
