"""ex34.py 获取列表元素"""

# 序数 ordinal number (1st, 2nd, 3rd, ...) == ordered, have to start from 1st
# 基数 cardinal number (0, 1, 2, 3, ...) == random accessed, cards at random
#       次序不重要，只是一个位置的记号/索引，可以直接去那个位置上存取，不用顺序访问

# address for each element == index

animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale']

# The animal at 1. [1] 'python3.6'
# The third (3rd) animal. [2] 'peacock'
# The first (1st) animal. [0] 'bear'
# The animal at 3. [3] 'kangaroo'
# The fifth (5th) animal. [4] 'whale'
# The animal at 2. [2] 'peacock'
# The sixth (6th) animal. ? index out of range
# The animal at 4. 'whale'

# print(animals[5])
