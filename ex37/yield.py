"""
Test 'yield' keyword
"""


def count_up_to(num):
    """a generator function: yield 0 to n, return a generator obj"""
    a_num = 0
    while a_num <= num:
        yield a_num  # yield the num each time
        a_num += 1


# 每次循环时，count_up_to() 执行到 yield，然后停止；
# 等到下一轮循环开始，再从上次停止的位置继续，执行到下一个 yield
for i in count_up_to(5):
    print(i)

# output 0, 1, 2, 3, 4 ,5
