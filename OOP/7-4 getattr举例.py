# __getaddr__ 举例

class A():
    name = "NoName"
    age = 18

    def __getattr__(self, name):
        print ('没找到没找到')
        print (name)

a = A()
print(a.name)
# 执行这句后会打印一个None,为什么？
# 你的函数本没有return数值，print后那就是个None
print(a.attr)