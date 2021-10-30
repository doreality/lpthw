def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

a = float(input("input a:"))
b = float(input("input b:"))
c = float(input("input c:"))
d = float(input("input d:"))
e = float(input("input e:"))

print("calculate (a+b)*c-(d/e)")

print("Directly:",(a+b)*c-(d/e))

print("Using the functions:", subtract(multiply(add(a,b),c), divide(d, e)))
