"""
Class key=value

.key

通过 instantiate 使用
"""


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


thing = MyStuff()  # instantiate 实例化 == create an object 创建一个对象
thing.apple()
print(thing.tangerine)
