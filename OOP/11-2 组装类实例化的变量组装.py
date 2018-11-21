from types import MethodType

def say(self):
    print("saying... ...")


class A():
    pass


a = A()

# 用实例化变量指定
a.say = MethodType(say, A)
a.say()