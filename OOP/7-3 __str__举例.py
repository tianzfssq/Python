# __str__ 举例

class A():
    def __init__(self,):
        print('哈哈我被调用了')

    def __call__(self):
        print('我又被调用了一次')

    def __str__(self):
        return '这是图灵学院的例子'
a = A()
print(a)
