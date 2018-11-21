class B():
    def __init__(self, name):
        print(name)

class C(B):
    def __init__(self, name):
        # 1. 调用父类构造函数
        # super(C, self).__init__(name)
        # python3.x上面的语句可以这样写
        super().__init__(name)

        # 2. 实现自己的构造函数
        print("这是C的功能")


c = C('我是C')