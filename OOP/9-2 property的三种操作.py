# 类属性 property三种操作
#- 除了普通的三种操作，还想增加点其他的操作，那么可以使用property完成

class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18

    #
    def fget(self):
        print("我被读取了")
        return self.name

    #
    def fset(self, name):
        print("我被写了，但还有好多事情")
        self.name = "图灵学院："+name

    def fdel(self):
        pass

        # property的四个参数位置是固定的
        # 第一个 读
        # 第二个 写
        # 第三个 删除
    name2 = property(fget, fset, fdel, "这是一个property的例子")


a = A()
print(a.name)

print(a.name2)