from sys import argv
# from os.path import exists

script, from_file, to_file = argv

# indata = open(from_file).read()

open(to_file, 'w').write(open(from_file).read())

# 文件操作没有把stream赋值给对象，所以不需要close()
