# 属性案例-2
# 定义一个Person类，基友name，age属性
# 对任意输入的姓名我们都希望使用大写保存
# 年龄， 我们希望我们统一使用整数保存
# x = property(fget, fset, fdel, doc)


class Person():
    # 函数名可以任意
    def fget(self):
        return self._name * 2
    def fset(self, name):
        # 名称已大写保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "name的说明文档")

p1 = Person()
p1.name = "TuLing"
print(p1.name) # 这句话不能直接调用，调用会报无_name属性错误

# 作业
# 1. 对age进行数据清洗，保存整数