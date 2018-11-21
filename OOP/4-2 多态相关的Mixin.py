
# 多继承实现功能扩展
class Person():
    name = 'fad'
    age = 18

    def eat(self):
        print("EAT......")

    def drink(self):
        print("DRINK......")

    def sleep(self):
        print("sleep......")


class Teacher(Person):
    def work(self):
        print("work...")

class Student(Person):
    def study(self):
        print("study...")


class Tutor(Teacher, Student):
    pass


t = Tutor()

print(Tutor.__mro__)

print(t.__dict__)

print(Tutor.__dict__)


print('*'*30)

#######################################

class TeacherMixin(Person):
    def work(self):
        print("work...")

class StudentMixin(Person):
    def study(self):
        print("study...")


class TutorM(Teacher, Student):
    pass

tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)