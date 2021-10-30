# ex15.py 阅读文件

# 不要 hard coding 简单粗暴地把txt的文件名放入代码

# 不要把应该从用户那里获取的信息，直接放在源代码里
# 因为我们随后会需要它载入别的文件
# （解耦）（数据复用）（好的可重用性）

# 用 argv 或者 input 来问用户打开哪个文件
# 而不是 hard coding 文件名


# 使用 sys 模块中的 argv 功能
from sys import argv

# 获取命令行参数 argv 并解包，获得源文件名称和要访问的文件名
script, filename = argv

# 打开名为 filename 的文件并把流返回给 txt 变量
# 创建文件对象（file object）
txt = open(filename)

# 输出提示信息
print(f"Here's your file {filename}:")
# 用 txt 执行 read() 命令，读出文件内容
# 使用 print() 是把读取的内容直接显示在命令行中
print(txt.read())

# 访问之后把文件关闭
txt.close()

# 利用 input() 方法让用再输入一遍文件名
print("Type the filename again:")
file_again  = input()

# 用 open() 打开文件，并把流返回给 txt_again 变量
txt_again = open(file_again)

# 让 txt_again 执行 read() 命令，读出文件内容
print(txt_again.read())

txt_again.close()



# read()
# 命令（command），函数（function），方法（method）

# sys 也叫包（package）
# agrv 是 sys 里面的功能（feature）