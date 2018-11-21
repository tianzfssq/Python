# 则不再继续向下查看except了
try:
    num = int(input('input your number:'))
    rst = 100/num
    print("计算结果是：{0}".format(rst))

# Exception为常规错误的基类
except Exception as e:
    print("我也不知道就出错了")
    print(e)
else:
    print("No Exception")
finally:
    print("反正会被执行")