# ex13.py 参数，解包，变量


# import 导入
# 把 Python 功能 库 中的功能（feature）添加到脚本
# feature（导入进来让Python做更多的事情）
# module 模块 e.g., 导入sys模块
# 有些程序员还叫做 libraries 库

# module == libraries == package
# import module : 导入整个模块  
# from module import feature : 导入模块中的某个功能

# argv = argument variable
# 当你运行 Python 脚本的时候
# 这个变量（variable）保存了你传给Python脚本的参数（argument）

from sys import argv

# 解包（unpack）了argv，而不是保留所有的参数，而是分成四个变量
script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)

# argv    获取用户在命令行运行脚本时的输入
# input() 让用户在程序运行的情况下输入