# ex6.py 字符串和文本

# 字符串可以包含任意数量多变量
# f"{var}"
# "some strings and {}".format(var)

# 声明数字变量 types_of_people
types_of_people = 10
# 声明字符串变量 x，并用格式字符串，插入 types_of_people
x = f"There are {types_of_people} types of people."

# 声明字符串变量 binary 和 do_not
binary = "binary"
do_not = "don't"
# 声明字符串变量 y，并把 binary 和 do_not 插入格式字符串
y = f"Those who know {binary} and those who {do_not}."

# 输出字符串 x 和 y
print(x)
print(y)

# 用格式字符串输出 x 和 y
print(f"I said: {x}")
print(f"I also said: '{y}'")

# 定义布尔型变量 hilarious
hilarious = 'hh{}'
# 定义字符串变量 joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

# 用格式 .format() 把 hilarious 插入到 joke_evaluation 并输出
# 多重 .format() 也可以
print(joke_evaluation.format(hilarious).format("hello{}").format("again"))

# 定义字符串变量 w 和 e
w = "This is the left side of..."
e = "a string with a right side."

# +: concatenation 把 w 和 e 拼接并输出
print(w + e)
# , 会有一个空格
print(w, e)
