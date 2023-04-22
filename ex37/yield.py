"""
Test 'yield' keyword
"""


def count_up_to(num):
    """a generator function: yield 0 to n, return a generator obj"""
    a_num = 0
    while a_num <= num:
        yield a_num  # yield the num each time
        a_num += 1


# the count_up_to() executes firstly,  then the loop.
for i in count_up_to(5):
    print(i)

# output 0, 1, 2, 3, 4 ,5
