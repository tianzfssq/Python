class Student():
    name = "daba"
    age = 18

    def doSomething(self):
        print("Do homework!")


print('类成员ID：',id(Student.name))
print('类成员ID：',id(Student.age))
print('*'*20)

s = Student()
print('对象实例ID：',id(s.name))
print('对象实例ID：',id(s.age))
print('对象实例：',s.__dict__)
print('*'*20)

s.name = 'testname'
s.age = 30

print('对象赋值后ID：',id(s.name))
print('对象赋值后ID：',id(s.age))
# 赋值后，对象a多了两个属性
print('对象赋值后ID：',s.__dict__)
print('*'*20)

class StudentA():
    name = "daba"
    age = 18

    # self 本身不是关键字，Python定义的是，第一个参数表示对象本身，self可以用普通变量代替
    def doSomething(self):
        self.name = 'aaaa'
        self.age = 99
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format(self.age))


yueyue = StudentA()
yueyue.doSomething()
print('*'*20)


class Teacher():
    name = "tianzf"
    age = 18

    def say(self):
        self.name = "ssq"
        self.age = '26'
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format(__class__.age))

    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print("hello, nice to see you again")

t = Teacher()
t.say()
# 调用绑定类函数使用类名, 这里不能使用t.sayAgain
# 使用实例化对象调用方法时，系统默认第一参数传对象本身，所以不带参数的方法只能用类实例调用
Teacher.sayAgain()


# 关于self的案例

class A():
    name = "liuying"
    age = 18

    def __init__(self):
        self.name = "aaa"
        self.age = "30"

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbbb"
    age = 888

a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()

# 此时，self被替换为a
A.say(a)

# 此时传入是实例B，B因为有name和age所以不会报错
A.say(B)
# 这里用了填鸭模型


# 私有变量案例
class Person():
    # name是共有的成员
    name = "liuying"
    # __age就是私有成员
    __age = 236

p = Person()
print(p.name)

# 这里无法方位__age
#print(p.__age)
print(p._Person__age)