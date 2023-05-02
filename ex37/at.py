"""
Decorator: @decorator above function
"""

import time


def time_it(func):
    """A decorator to calculate function execution time"""
    def wrapper(*args, **kwargs):
        """Actually substitute origin func"""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.8f} seconds to run.")
        return result
    return wrapper


@time_it
def some_function():
    """A simple hello func"""
    print("Hello World")
    for i in range(2000):
        print(i, end='')
    print('\n')


# equivalent way to @time_it
# some_function = time_it(some_function)

some_function()
