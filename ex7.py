"""ex7.py 更多打印"""

print("Mary had a little lamb.")
# 比较短的字符串应该用单引号，而长的用双引号
# 但是 Python 里用哪个都一样（不同于 C ）
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?: print ten times '.'

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.
# end(' ')
# make the first print ending with a ' ' not '\n'
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
