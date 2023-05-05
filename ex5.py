"""
ex5.py 更多变量和打印

字符串 是你让计算机呈现给人看的内容
打印字符串、把字符串保存到文件、发送到网络服务器等

格式字符串——把变量加入字符串中输出：
print(f"some strings, {somevar}.")
"""

name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# round() 四舍五入
height_cm = round(height * 2.54)  # 1 inch = 2.54 cms
weight_kg = round(weight * 0.4535924)  # 1 lb = 0.4535924 kgs

print(f"Let's talk about {name}.")
print(f"He's {height} inches ({height_cm} centimeters) high.")
print(f"He's {weight} pounds ({weight_kg} kilograms) heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
