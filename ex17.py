"""ex17.py 更多文件"""

# 把一个文件复制成另一个

from sys import argv
from os.path import exists

# test.txt -> new_test.txt
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

# exists() 基于字符串中的变量文件名来判断
# 如果文件存在，返回 True；否则返回 False
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# 练习 17 会话
# # first make a sample file
# echo "This is a test file." > test.txt
# # then look at it
# cat test.txt
# This is a test file.
# # now run our script on it
# python3.6 ex17.py test.txt new_file.txt
# Copying from test.txt to new_file.txt
# The input file is 21 bytes long
# Does the output file exist?
# False
# Ready, hit RETURN to continue, CTRL-C to abort.
# Alright, all done.
