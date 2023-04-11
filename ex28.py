print("True and True: True ", True and True)
print("False and True: False ", False and True)
print("1 == 1 and 2 == 1: False ", 1 == 1 and 2 == 1)
print("'test' == 'test': True ", 'test' == 'test')
print("1 == 1 or 2 != 1: True ", 1 == 1 or 2 != 1)
print("True and 1 == 1: True ", True and 1 == 1)
print("False and 0 != 0: False ", False and 0 != 0)
print("True or 1 == 1: True ", True or 1 == 1)
print("'test' == 'testing': False ", 'test' == 'testing')
print("1 != 0 and 2 == 1: True ", 1 != 0 and 2 == 1)  # False
print("'test' != 'testing': True ", 'test' != 'testing')
print("'test' == 1: False ", 'test' == 1)
print("not (True and False): True ", not (True and False))
print("not (1 == 1 and 0 != 1): False ", not (1 == 1 and 0 != 1))
print("not (10 == 1 or 1000 == 1000): False ", not (10 == 1 or 1000 == 1000))
print("not (1 != 10 or 3 == 4): False ", not (1 != 10 or 3 == 4))
print("not ('testing' == 'testing' and 'Zed' == 'Cool Guy'): True ",
      not ('testing' == 'testing' and 'Zed' == 'Cool Guy'))
print("1 == 1 and (not ('testing' == 1 or 1 == 0)): True ",
      1 == 1 and (not ('testing' == 1 or 1 == 0)))
print("'chunky' == 'bacon' and (not (3 == 4 or 3 == 3)): False ",
      'chunky' == 'bacon' and (not (3 == 4 or 3 == 3)))
print("3 == 3 and (not ('testing' == 'testing' or 'Python' == 'Fun')): False ",
      3 == 3 and (not ('testing' == 'testing' or 'Python' == 'Fun')))

# Boolean logic expression
# 返回布尔表达式的运算数，不仅仅只是 True 和 False
# (1 and 1) return 1
# (2 and 2) return 2
# (True and 1)  return 1
# (False or 1) return 1
# ('test' and 'test') return 'test'
