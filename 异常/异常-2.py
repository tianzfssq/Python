# 多种异常案例
# 需要把越具体的错误往前放
# 在处理异常的时候，一旦拦截到某个异常，
# 则不再继续向下查看except了
try:
    num = int(input('input your number:'))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
except ZeroDivisionError as e:
    print("error")
    print(e)
    exit()
except NameError as e:
    print("名字起错了")
    print(e)
    exit()

# Exception为常规错误的基类
except Exception as e:
    print("我也不知道就出错了")
    print(e)
    exit()

print("hahahah")
# 作业：为什么我们可以直接打印出实例e，此时实例e应该实现了那些函数