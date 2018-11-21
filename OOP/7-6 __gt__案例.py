# __gt__举例

class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        # 使用self定义个属性，必须使用self调用？
        # 下面直接调用_name会报错？？
        print("哈哈，{0}会比{1}大吗".format(self._name, obj._name))
        return self._name > obj._name



stu1 = Student("one")
stu2 = Student("two")

print(stu1 > stu2)