# ex20.py 函数和文件

# 函数和文件一起工作并发挥作用

# 导入 sys 包，使用 argv feature
from sys import argv

# 解包，得到要操作的文件名
script, input_file = argv

# 定义 print_all() 函数
# f 作为文件指针
# 读 f，输出内容


def print_all(f):
    print(f.read())

# 定义 rewind() 函数
# f 作为文件指针
# 通过 seek(0) 回到文件读写的开头


def rewind(f):
    f.seek(0)

# 定义 print_a_line() 函数
# line_count 传入行号，f 作为文件指针
# 用 readline() 输出文件的一行内容
# 当 readline() 发现一个 \n 字符，会停止扫描并停在这个位置


def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')


# 打开文件，返回给 current_file
current_file = open(input_file)

print("First let's print the whole file:\n")
# 调用 print_all() 输出文件
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# 调用 rewind() 回到文件开头
rewind(current_file)

print("Let's print three lines:")
# current_line 记录行号
current_line = 1
# 读文件第 1 行
print_a_line(current_line, current_file)
# +1，现在读第 2 行
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
# +1, 现在读第 3 行
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
