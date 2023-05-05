"""
Test `try`, `except`, `finally`, `raise` keyword

Two ways to use try-except:
  1. 指定具体要捕获的异常，例如 ValueError，TypeError
  2. 如果不指定，就要 log fully stack trace，
     否则很容易出现捕获了异常但是不知道到底发生了什么
     在 except Exception as ex:
       logging.exception('Caught an error.')

Common exceptions:
    ImportError
    IndexError
    NameError
    SyntaxError
    TypeError
    ValueError
"""
try:
    print(1)
    print(2 / 0)  # Zero Division
    # print('a' + 1) # Type error
except ZeroDivisionError:
    print("Division is Zero!")
except ValueError:
    print('Value is not expected')
except TypeError:
    print('Type is wrong')
else:  # only execute when try is done completely (no exception)
    print('hello')
finally:  # print anyway, after try or except
    print('Print anyway.')
