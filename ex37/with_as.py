"""
Test 'with EXPRESSION as VARIABLE' keyword

with..as 在用完之后要显式关闭 / 释放的资源
files, network sockets, or database connections.
"""

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('Hello world!')

# file will be closed automatically
