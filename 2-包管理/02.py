import importlib

tuling = importlib.import_module("01")

stu = tuling.Student("xiaojing",20)

stu.say()

tuling.sayHello()