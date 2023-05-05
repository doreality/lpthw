"""
ex18.py 名称，变量，代码，函数

函数
1. 为代码起名字
2. 像脚本获取 argv 一样获取参数（arguments）
3. 通过 1 和 2 的操作，可以做一些"小脚本"或"微命令"
"""

# 通过 def 来创建函数

# this one is like your scripts with argv


def print_two(*args):
    """ get arguments in a list, and print them out 
        *args 将所有的参数都存入 args, 成为一个列表 """
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    ''' get two arguments, and print them out '''
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    ''' get one arg and print it out '''
    print(f"arg1: {arg1}")


def print_none():
    ''' take no arg '''
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
