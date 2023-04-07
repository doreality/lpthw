# ex20.py 函数和文件

# 函数和文件一起工作并发挥作用

# 导入 sys 包，使用 argv feature
from sys import argv

# 解包，得到要操作的文件名
script, input_file = argv


def print_all(f):
    '''定义 print_all() 函数
       f 作为文件指针
       读 f，输出内容'''

    print(f.read())


def rewind(f):
    '''定义 rewind() 函数
       f 作为文件指针
       通过 seek(0) 回到文件读写的开头'''

    f.seek(0)


def print_a_line(line_count, f):
    '''定义 print_a_line() 函数
       line_count 传入行号, f 作为文件指针
       用 readline() 输出文件的一行内容
       当 readline() 发现一个 \\n 字符，会停止扫描并停在这个位置'''

    print(line_count, f.readline())


# 打开文件，返回给 current_file
current_file = open(input_file, 'r', encoding='utf-8')

print("First let's print the whole file:\n")
print_all(current_file)  # 调用 print_all() 输出文件

print("Now let's rewind, kind of like a tape.")
rewind(current_file)  # 调用 rewind() 回到文件开头

print("Let's print three lines:")

current_line = 1  # current_line 记录行号
print_a_line(current_line, current_file)  # 读文件第 1 行

# current_line = current_line + 1
current_line += 1  # +1，现在读第 2 行
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1  # +1, 现在读第 3 行
print_a_line(current_line, current_file)
