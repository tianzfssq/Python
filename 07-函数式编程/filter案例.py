# filter案例

def isEven(a):
    return a%2 == 0


l = [1,2,3,5,6,6,9,8,7,2]

rst = filter(isEven, l)

# 写法一
#print(list(rst))

# 写法二

print([i for i in rst])
