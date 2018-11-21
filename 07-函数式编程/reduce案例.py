# reduce案例
from functools import reduce

# 定义一个操作函数
def myAdd(x,y):
    return x+y

rst = reduce(myAdd, [i for i in range(10)])

print (rst)