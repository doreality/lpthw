# ex19.py 函数和变量

# 函数里的变量和脚本里的变量没有关系

# 定义函数 cheese_and_crackers
# 参数 cheese_count 接收数字
# 参数 boxes_of_crackers 接收数字
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


print("We can just give the function numbers directly:")
# 调用函数，直接传入数字
cheese_and_crackers(20, 30)

print("OR, we can use variables from out script: ")
# 定义两个变量
amount_of_cheese = 10
amount_of_crackers = 50
# 调用函数，用变量传参数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ")
# 调用函数，可以用数字的算术运算进行传参数
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math: ")
# 调用函数，可以把变量和数字运算进行参数传入
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
