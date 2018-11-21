# 构造函数的概念

class Dog():
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化所得名
    def __init__(self):
        print('i am init in dog')

# 实例化的时候，括号内的参数需要跟构造函数参数匹配
#kaka = Dog()



# 继承中的class

class Animal():
    pass

class PaxingAni():
    pass

class DogDog(PaxingAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化所得名
    def __init__(self):
        print('i am init in dog')

kaka = DogDog()

print(type(super))