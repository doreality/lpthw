# LPTHW 索引表

## 命令



### macOS



### Linux



### Windows



## 函数



### 创建函数

- 你是否用`def`来创建函数了？
- 你的函数名是只包含字符和`_`（下划线）吗？
- 你在函数名后面放`(`（左圆括号）了吗？
- 你在左圆括号后面放参数（argument）了吗？参数之间是以逗号隔开的吗？
- 你的每个参数都是唯一的（即没有重名）吗？
- 你在参数后面放`)`（右圆括号和`:`冒号了吗
- 你在与这个函数相关的代码行前面加上四个空格的缩进了吗？（不能多，也不能少）
- 你是通过另起一行不缩进来结束你的函数的吗？



### 运行（使用或调用）一个函数



run / use / call



- 你是通过输入函数名称来运行/调用/使用一个函数的吗？
- 你运行的时候又在名称后面加`(`吗？
- 你有把你想要的值放在圆括号里并用逗号隔开了吗？
- 你是以`)`来结束调用这个函数的吗？



## 复习



截至练习20，使用过的单词和符号



| 符号                         | 名字                           | 作用                                                         |
| ---------------------------- | ------------------------------ | ------------------------------------------------------------ |
| print()                      | 打印                           | 把括号里的内容输出到显示屏上                                 |
| #                            | 井号                           | 注释一行代码，使其不执行                                     |
| +                            | 加号 plus                      | 算术运算，两个数相加                                         |
| -                            | 减号 minus                     | 算术运算，两个数相减                                         |
| *                            | 星号 asterisk                  | 算术运算，两个数相乘（或者指针）                             |
| /                            | 斜杠 slash                     | 算术运算，两个数相除                                         |
| %                            | 百分号 percent                 | 算术运算，两个数求模（取余数）                               |
| <                            | 小于号，less-than              | 比较；结果为真返回 Ture，否则返回 False                      |
| <=                           | 小于等于号，less-than-equal    | 比较；结果为真返回 Ture，否则返回 False                      |
| >                            | 大于号，greater-than           | 比较；结果为真返回 Ture，否则返回 False                      |
| >=                           | 大于等于号，greater-than-equal | 比较；结果为真返回 Ture，否则返回 False                      |
| =                            | 等号，equal                    | 赋值                                                         |
| ==                           | 双等号，double-equals          | 比较；相等则返回 True，否则返回 False                        |
| f"{variable}"                | 格式字符串                     | 用{}把变量variable加到字符串中                               |
| round()                      | 大约                           | 四舍五入                                                     |
| "{}{}...".format(var1,2,...) | 格式字符串                     | 用多个{}把多个变量加到字符串中                               |
| """ """                      | 格式字符串                     | 引号中的字符串保留输入的格式（可以带回车）                   |
| \                            | 转义字符 escape sequence       | 可以把没法输入的字符转化为字符串                             |
| `\\`                         | 反斜杠 backslash               |                                                              |
| `\'`                         | 单引号 single-quote            |                                                              |
| `\"`                         | 双引号 double-quote            |                                                              |
| `\a`                         | 响铃 BEL                       | ASCII bell                                                   |
| `\b`                         | 退格 BS                        | ASCII backspace                                              |
| `\f`                         | 换页 FF                        | ASCII formfeed                                               |
| `\n`                         | 换行 LF                        | ASCII linefeed，将当前位置下移一行                           |
| `\r`                         | 回车 CR                        | ASCII carriage，将当前位置移到本行开头                       |
| `\t`                         | 水平制表 HT                    | ASCII horizontal tab，跳到下一个 TAB 位置                    |
| `\v`                         | 垂直制表 VT                    | ASCII vertical tab                                           |
| `\N{name}`                   |                                | 在Unicode数据库中命名为name的字符                            |
| `\uxxxx`                     |                                | Unicode字符，16位十六进制                                    |
| `\Uxxxxxxxx`                 |                                | Unicode字符，32位十六进制                                    |
| `\ooo`                       |                                | 八进制所表示的任意字符oo                                     |
| `\xhh`                       |                                | 十六进制所表示的任意字符hh                                   |
| end=''                       | 结尾不自动换行                 | 放在字符串末尾，例如print()的结尾处，print()的输出不自动换行 |
| input("something")           | 输入                           | 输出"something"给用户，从用户处读取输入，将输入返回，返回值是字符串格式 |
| int()                        | 类型转换函数                   | 把括号中的参数强制转换为int型返回                            |
| type()                       | 类型显示                       | 返回参数的数据类型                                           |
| sys                          | 系统                           | 系统模块（module）或sys包（package）或者库（libraries）      |
| import                       | 导入                           | 导入整个模块(import module)，调用功能module.feature；从模块中导入功能（from module import feature），调用功能直接用feature |
| module                       | 模块                           | python的脚本名：模块名.py                                    |
| argv                         | 参数变量                       | 获取用户输入的命令行参数                                     |
| unpack                       | 解包                           | 把一个变量可以切分赋值给多个变量（变量1，变量2，……=argv）    |
| obj=open(filename,'way')     | 打开文件                       | 以way（读或者写或者什么）方式打开名为filename的文件，并返回stream给obj作为文件对象（file object） |
| obj.read()                   | 读文件                         | 利用obj读文件的内容，可以把文件内容全部获取并赋值给一个变量  |
| obj.close()                  | 关闭文件                       | 对文件进行访问之后，一定要关掉                               |
| obj.readline()               | 读文件一行                     | 读文本文件的一行内容，发现一个`\n`，会停在当前位置           |
| obj.truncate()               | 清空文件                       | 清空时要当心                                                 |
| obj.write("sth")             | 写文件                         | 给文件写一些sth                                              |
| obj.seek(0)                  | 读写位置移到到最开头           | 把读写文件到位置移动到文件的最开头                           |
| `'r'`                        | open()的参数                   | open for reading (default)                                   |
| `'w'`                        | open()的参数                   | 如果是`'w'`方式打开文件且文件已经存在，那么会被清空          |
| `'x'`                        | open()的参数                   | create a new file and open it for writing                    |
| `'a'`                        | open()的参数                   | open for writing, appending to the end of the file if it exists |
| `'b'`                        | open()的参数                   | binary mode                                                  |
| `'t'`                        | open()的参数                   | text mode (default)                                          |
| `'+'`                        | open()的参数                   | open a disk file for updating (reading and writing)          |
| `'U'`                        | open()的参数                   | universal newline mode (deprecated)                          |
| `'rt'`                       | open()的参数                   | default mode                                                 |
| os.path                      | module                         |                                                              |
| exists(string)               | method in os.path              | 基于string字符串中的变量文件名来判断：如果文件存在，返回True；否则返回False |
| def                          | 关键字，用来创建函数           | def+空格+函数名+括号+冒号，另起一行空4格缩进都是函数的内容   |
| i += 1                       | 运算符                         | i = i + 1                                                    |
| float()                      | 强制转换                       | 强制转换为单精度浮点数                                       |





