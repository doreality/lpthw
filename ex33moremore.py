def make_list(end_num, step):
    """make a number list from 0 to end_num"""

    numbers = list(range(0, end_num, step))

    print("The numbers: ")

    for num in numbers:
        print(num)


make_list(10, 2)
