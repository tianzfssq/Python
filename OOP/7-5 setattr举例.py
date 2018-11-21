# __setattr__举例

class Person():
    def __init__(self):
        pass


p = Person()
print(p.__dict__)

# 下面语句能够正常执行
# 和C++不一样？？ 没有age属性为什么赋值不会出错？？？？？？？？？？？？？？？？
p.age = 18
print(p.age)


class PersonA():
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print("设置属性：{0}".format(key))

        # 下面语句会导致死循环
        #self.name = value
        # 此种情况，为了避免死循环，规定统一调用父类魔法函数
        supper().__setattr__(key, value)


pa = PersonA()
# 这里就有会报错了，因为我们重写了__setattr__函数，
# 所以没有调用默认__setattr__函数，导致无法添加新属性
pa.age = 18
print(pa.age)