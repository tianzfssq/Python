# __mro__用法

print('mro用法：')
class A():
    pass

class B(A):
    pass

print(A.__mro__)
print(B.__mro__)

print('*'*30)


# 继承

class Fish():
    def __init__(self, name):
        self.name = name    # self表示这个name是属于Fish类的，类似C++定义了一个成员属性

    def swim(self):
        print("i am swming")

class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("i am fly....")

class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("i am workding...")

class SuperMan(Person, Fish, Bird):
    def __init__(self, name):
        self.name = name


print(SuperMan.__mro__)
p = SuperMan('yueyue')
p.fly()
p.swim()

print('*'*30)

class A():
    def __init__(self):
        print('this is A')

class B(A):
    def __init__(self):
        print('this is B')

class C(B):
    pass

#下面语句仅执行了B的构造函数
c = C()



class BB(A):
    def __init__(self, name):
        print('this is B')
        print(name)


class CC(BB):
    pass

cc = CC()