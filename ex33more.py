def make_list(end_num, step):
    """make a number list from 0 to end_num"""
    i = 0
    numbers = []

    while 0 <= i < end_num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


make_list(10, -1)
