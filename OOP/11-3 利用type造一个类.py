#利用type造一个类


# 先给类定义几个函数
def say(self):
    print("Saying......")

def talk(self):
    print("talking......")

A = type("AName", (object,), {"class_say":say, "class_talk":talk})

a = A()

a.class_talk()
