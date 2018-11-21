
class Person():
    '''
    这是一个人，一个高尚的人，
    他还有属性
    '''
    # 函数名可以任意
    def fget(self):
        return self._name * 2
    def fset(self, name):
        # 名称已大写保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "name的说明文档")

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)