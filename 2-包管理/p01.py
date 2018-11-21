# 包含一个学生类
# 一个sayhello函数
# 一个打印语句

class Student():
    def __init__(self, name = 'NoName', age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print('Hi,欢迎来到图灵学院！')

# 这句导入时，会输出
# import相当于把导入文件内容直接赋值到被导入文件
# print("我是一个模块")

# 若是直接执行此文件，__name__为__main__
# 若被此文件被导入，则__name__为 p01
print(__name__)

if __name__ == '__main__':
    print("我是一个模块")