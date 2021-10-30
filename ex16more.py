from sys import argv

script, filename = argv

print(f"Now open the file {filename}...")
# 'w' for writing 
# (truncating the file if it already exists)
target = open(filename, 'w+')

print("Input something to the file:")
line1 = input("Input line1: ")
line2 = input("Input line2: ")
line3 = input("Input line3: ")

print("Now write the file {}".format(filename))
target.write("line1:{}\nline2:{}\nline3:{}\n".format(line1, line2, line3))

# seek(0) 读、写位置移到最开头
target.seek(0)

print("Now the file is:")
print(target.read())

print("Now close the file.")
target.close()

# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)

# default mode is 'rt'