# 自己组装类

# 定义一个函数
# 注意一点：say的参数,若要赋值给class，
# 必须有一个变量，因为class的成员函数被调用时默认会传递self给他
def say(self):
    print("saying... ...")


class A():
    pass

# 这里调用需要添加一个参数
#say(9)

# 用类指定
A.say = say

a = A()
a.say()
