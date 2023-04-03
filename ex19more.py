# from sys import argv

# script, goal = argv

def bjyxszd(scores):
    print(f"bjyx {scores}")

# # 1 directly
# bjyxszd(95)

# # 2 use variable
# fate = 95
# bjyxszd(fate)

# # 3 use user input
# bjyxszd(input("input the scores of bjyx: "))

# # 4 = 2 + 3
# score = input("Input score: ")
# bjyxszd(score)

# # 5 use in def
# def embedded():
#     bjyxszd(95)
# embedded()

# # 6 use the unpack part of argv
# bjyxszd(goal)

# # 7 use convert
# bjyxszd(int(fate))

# # 8 use math
# bjyxszd(90 + 5)

# # 9 use no input?
# error missing 1 required positional argument
# bjyxszd()


# 10 use variable to call(but no return?)
# 可以执行！
# 没有返回值的函数给变量赋值，是无意义的
# 结果就是函数会执行，但是变量是 NoneType
score = 95
have_a_try = bjyxszd(score)
print(type(have_a_try))  # 'NoneType'
