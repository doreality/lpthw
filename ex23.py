# ex23.py 字符串，字节和字符编码

# encode / decode => bytes

import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:  # readline() 到达文件尾会返回空字符串，递归出口
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)  # recursion


def print_line(line, encoding, errors):
    next_lang = line.strip()  # strip() 去除首尾空白部分
    raw_bytes = next_lang.encode(encoding, errors=errors)  # string.encode()
    cooked_string = raw_bytes.decode(encoding, errors=errors)  # bytes.decode()

    print(raw_bytes, "<===>", cooked_string)


# languages = open("languages.txt", encoding="utf-8")
languages = open("encoding.txt", encoding="gbk")

main(languages, encoding, error)

# DBES: Decode Bytes, Encode Strings
# Bytes => String: Bytes.decode()
# String => Bytes: String.encode()
