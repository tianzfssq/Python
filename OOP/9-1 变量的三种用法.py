class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18

a = A()

# 属性的三种用法
# 1. 赋值
# 2. 读取
# 3. 删除

# 赋值
a.name = "田老师"

# 读取
print(a.name)

# 删除
del a.name
# print(a.name) # 报错

