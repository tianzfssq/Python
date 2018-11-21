# 继承的用法
# 在python中，任何一个类都有一个共同的父类叫object
# 若类不继承自任何自定义类，则()可以省略 ， 下面可以写成 class Person:
class Person():
    name = "NoName"
    age = 0

    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = "sec" #小名，是保护的，子类可以用，但不能共用
    def sleep(self):
        print('Sleeping......')


# 父类写在括号内
class Teacher(Person):
    teacher_id = 11
    def make_test(self):
        print('attention')

t = Teacher()

print(t.name)

# 受保护不能外部访问，为啥这里可以？？？？
print(t._petname)

# 私有访问问题
# 公开访问私有变量是不允许的
#print(t.__score)

t.sleep()
print(t.teacher_id)
t.make_test()