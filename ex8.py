# ex8.py 打印，打印

# 更复杂的格式字符串

formatter = "{} {} {} {}"

# format()函数，把{}替换成参数变量
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# True 和 False 是 Python 的关键字，表示“对”和“错”
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
