# 抽象

class Ab()

    def sayHello(self):
        # 不实现，这里虽然定义了但是子类可以实现也可以不实现，无法规范子类行为
        pass


class Dog(Ab):

    def sayHello(self):
        print ("smell")


class Person(Ab):
    def sayHello(self):
        print ("kiss me")