"""
ex16.py 读写文件

记住命令：
close() - 关闭文件，"文件->另存为"
read() - 读取文件内容，可以把读取结果赋给一个变量
readline() - 只读取文本文件的一行内容
truncate() - 清空文件。清空时要当心
write('stuff') - 给文件写 'stuff'
seek(0) - 把读、写的位置移到文件的最开头
"""

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that , hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

#  'w' 参数：通过明确说明你要写入一个文件，安全地打开它
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
