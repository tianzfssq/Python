# 闭包常见坑

def count():
    fs = []
    for i in range(1,4):
        # 定义了一个函数f
        # f使用了外部参数，f是一个闭包
        def f():
            return i*i
        fs.append(f)

    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

#返回值都等于9

### 出现的问题：
# 造成上述状况的原因是：返回函数使用了外部变量i，i并非立即执行，
# 而是等到三个函数都返回的时候才统一执行，此时i已经变为3，最终调用时返回的都是3*3