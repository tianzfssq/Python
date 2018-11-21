# 简单异常案例
try:
    num = int(input('input your number:'))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
except:
    print("error")
    exit()