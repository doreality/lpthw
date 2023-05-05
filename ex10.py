"""
ex10.py 那是什么？

\ 转义字符 escape sequence
可以把没法输入的字符转化为字符串

转义单引号和双引号
1. 用 \' 和 \"
2. 用三个双引号
"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

Grass = "sweeties \a"
fat_cat = '''
"""
I'll do a list: # a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* {}
"""
'''.format(Grass)

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
