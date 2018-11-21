from pkg02 import *

stu = p01.Student()
stu.say()

# 下面语句无法执行，因为__init__文件中定义了__all__，只导入了模块
# inInit()