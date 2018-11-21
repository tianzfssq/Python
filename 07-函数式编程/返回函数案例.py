# 返回函数案例
def myF(a):
    print("In myF")
    return None

a = myF(8)
print(a)

print("*****************************")
# 函数作为返回值返回，被返回的函数再函数体内定义

def myF2():
    def myF3():
        print("in myF3")
        return 3
    return myF3

f3 = myF2()
print(type(f3))
print(f3)

f3()
print("*****************************")

# 复杂一点的例子

# args:参数列表
# 1. myF4定义函数，返回内部函数myF5
# 2. myF5使用了外部变量，这个变量是myF4的参数
def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5

# 注意这里与C++感觉不太一样
# myF4直接把参数赋值了, 下面调用 f5 和 f6，相当于调用的 myF5
# 但是myF5函数体内的args已经赋值了！！
# 这种结果叫闭包，详见note.md闭包解释
f5 = myF4(1,2,3,4,5,6,7)
f6 = myF4(10,20,30,40,50,60,70)
print(f5())
print(f6())


