"""ex30.py Else 和 if"""

people = 30
cars = 40
trucks = 15

if cars > people:  # 如果 cars 比 people 多
    print("We should take the cars.")
elif cars < people:  # 否则如果 cars 比 people 数量少
    print("We should not take the cars.")
else:  # 否则（cars 和 people 数量相同）
    print("We can't decide.")

if trucks > cars:  # 如果 trucks 比 cars 数量多
    print("That's too many trucks.")
elif trucks < cars:  # 否则如果 trucks 比 cars 数量少
    print("Maybe we could take the trucks.")
else:  # 否则（trucks 和 cars 数量相同）
    print("We still can't decide.")

if people > trucks:  # 如果 people 比 trucks 多
    print("Alright, let's just take the trucks.")
else:  # 否则（people 少于或等于 trucks
    print("Fine, let's stay home then.")
