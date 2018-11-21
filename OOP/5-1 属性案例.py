# 属性案例
# 创建Student类，描述学生类
# 学生具有Student.name
# 但name格式并不统一

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("hey, my name is {0}".format(self.name))

    def setName(self):
        self.name.toUpper()

s1 = Student("LIU Ying", 19)
s2 = Student("ma yun", 19)

s1.intro()
s2.intro()