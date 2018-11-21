# 元类演示

# 元类写法是固定的，必须继承自type
# 元类一般命名以MetaClass结尾

class TulingMetaClass(type):

    #  注意写法
    def __new__(cls, name, bases, attrs):
        print("我是元类")
        attrs["id"] = '000000'
        attrs['addr'] = 'BeiJing'
        return type.__new__(cls, name, bases, attrs)

class Teacher(object, metaclass=TulingMetaClass):
    pass


t = Teacher()

t.id