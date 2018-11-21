'''
定义一个学生类，用来形容学生
'''

# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass


# 定义一个对象
mingyue = Student()


# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'python'

    # 需要注意的
    # 1. def doHomework的缩进层级
    # 2. 系统默认一个self参数
    def doHomework(self):
        print('I 在做作业')

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yueyue的学生，yueyue为对象实例
# PythonStudent为类实例，
# !!!注意!!!(和C++不同，类实例有自己的存储空间)：类实例和对象实例都有自己的存储空间，存储自己的数据******
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传入参数
yueyue.doHomework()

PythonStudent.__dict__
print('---------')
yueyue.__dict__