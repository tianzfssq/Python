# 自定义异常
# 注意： 自定义类必须继承系统异常类

class DanaError(ValueError):
    pass


try:
    print("I love wangxiaojing")
    print(3.1415926)
    # 手动引发异常
    # 注意语法： raise ErrorClassName
    raise DanaError
    print("还没完了呀")
except NameError as e:
    print("NameError...")
except DanaError as e:
    print("DanaError...")
except ValueError as e:
    print("ValueError...")
except Exception as e:
    print("ValueError...")
finally:
    print("我肯定被执行")

