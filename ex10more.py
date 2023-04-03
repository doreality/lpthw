# Escape Sequences List

print("Backslash: \\")

print("Single-quote: \'")

print("Double-quote: \"")

# 响铃(BEL)
print("ASCII bell(BEL): \a")

# 退格(BS) ，将当前位置移到前一列
print("ASCII backspace(BS): \b")

# 换页(FF)，将当前位置移到下页开头
print("ASCII formfeed(FF): \f")

# 换行(LF) ，将当前位置移到下一行
print("ASCII linefeed(LF): \n")

print("Character named name in the Unicode database(Unicode only): \N{LF}")

# 回车(CR) ，将当前位置移到本行开头
print("ASCII carriage return(CR): \r")

# 水平制表(HT) （跳到下一个TAB位置）
print("ASCII horizontal tab(TAB): \t")

print("Character with 16-bit hex value xxxx(Unicode only): \u1234")

print("Character with 32-bit hex value xxxxxxxx(Unicode only): \U0001f4a5")

# 垂直制表(VT)
print("ASCII vertical tab(VT): \v")

# 八进制代表的任意字符
print("Character with octal value: \101")

# 十六进制所代表的任意字符 1111 1111
print("Character with hex value: \xFF")

# Unix系统里，每行结尾只有"<换行>"，即"\n"
# Windows系统里面，每行结尾是"<回车><换行>"，即"\r\n"
# Mac系统里，每行结尾是"<回车>"，即"\r"
# 现在的macOSX结尾是"<换行>","\n"
# 一个直接后果是，Unix/Mac系统下的文件在Windows里打开的话，所有文字会变成一行；
# 而Windows里的文件在Unix/Mac下打开的话，在每行的结尾可能会多出一个^M符号。
