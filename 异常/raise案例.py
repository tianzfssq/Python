# raise案例

try:
    print("I love wangxiaojing")
    print(3.1415926)
    # 手动引发异常
    #注意语法： raise ErrorClassName
    raise ValueError
    print("还没完了呀")
except NameError as e:
    print("NameError...")
except ValueError as e:
    print("ValueError...")
except Exception as e:
    print("ValueError...")
finally:
    print("我肯定被执行")
    
