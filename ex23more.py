bytes = b'\xcc\xec\xb5\xd8\xd0\xfe\xbb\xc6\xa3\xac\xd3\xee\xd6\xe6\xba\xe9\xbb\xc4\xa1\xa3'
str = bytes.decode(encoding='gbk')
print(str)

# gbk 通过两个字节来编码，所以删除的是2的倍数，就可以破坏字符串，但是又能通过解码