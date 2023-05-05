"""
ex11.py 问问题

* 从用户那里获得输入
* 改一改
* 打印出一些东西以显示它变成了什么
"""

# end=' ' 是为了让 print() 以空格结束，而不是换行
print("How old are you?", end=' ')
age = input()  # input() 和用户交互，得到用户的输入
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# python3.x 中的 input() 默认接收的是 字符串 str

x = int(input("input x:"))  # int() 强制转换为 int 类型
print(type(x))  # type() 返回的是 x 的类型
