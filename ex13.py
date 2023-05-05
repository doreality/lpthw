"""
ex13.py 参数，解包，变量


import(导入): 把 Python 功能库中的功能（feature）添加到脚本

feature == module == library
feature: 导入进来让Python做更多的事情
module(模块): e.g., 导入 sys 模块 import sys
有些程序员还叫做 libraries 库

import module: 导入整个模块
from module import feature : 导入模块中的某个功能(变量/类/函数)
from package import module as md

argv: argument variable
当你运行 Python 脚本的时候
这个变量（variable）保存了你传给 Python 脚本的参数（argument）
参数是字符串
"""

from sys import argv

# 解包（unpack）了 argv，不是保留所有的参数，而是分成四个变量
script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)

# argv    获取用户在命令行运行脚本时的输入
# input() 让用户在程序运行的情况下输入

another = input(('Please input another variable: '))
print('Variable got by input():', another)
