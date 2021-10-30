# ex11.py 问问题

# 终于要放数据啦～！

# * 从用户那里获得输入
# * 改一改
# * 打印出一些东西以显示它变成了什么

# input 是什么～

# 末尾放 end=' ' 是为了让print()不要另一起行
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# python3.x 中的 input() 默认接收的是 字符串 str

x = int(input("input x:")) # 进行一下强制转换
print(type(x))