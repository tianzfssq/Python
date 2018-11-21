# lambda表达式
# 1. 以lambda开头
# 2. 紧跟一定的参数（如果有的话）
# 3. 参数后用冒号和表达式主体隔开
# 4. 只是一个表达式，没有return

stm = lambda x:x*100

print(stm(89))


stm2 = lambda x,y,z:x + y*10 + z*100

print(stm2(1,2,3))
