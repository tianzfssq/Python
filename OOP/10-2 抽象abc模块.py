# 抽象类的实现
import abc

# 声明一个类并指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def smoking(self):
        pass

    @abc.abstractmethod
    def drink(self):
        pass

    @ abc.abstractmethod
    def play(self):
        pass

class ZGHuman(Human):
    def smoking(self):
        print("中南海")

    def drink(self):
        print("茅台")

    def play(self):
        print("唱歌")

# 如果ZGHuman有个函数未实现，则它不允许被实例化
a = ZGHuman()

a.play()