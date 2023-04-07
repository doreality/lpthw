from sys import argv

script, first, second, third = argv

print("The first number is:", first)

print("The second number is:", second)

print("The third number is:", third)

fourth = input("The next is:")

print("The fouth number is:", fourth)

# 全是 <class 'str'>
print(type(script), type(first), type(second), type(third), type(fourth))
