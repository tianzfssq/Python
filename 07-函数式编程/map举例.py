# map举例
l1 = [i for i in range(10)]

def mulTen(n):
    return n*10

l2 = map(mulTen, l1)

# map类型是一个可迭代的结构，所以可以使用for
print(type(l2))
print(l2)

for i in l2:
    print(i)

# 由于map返回值是一个可迭代的结构，所以生成列表下面方式是不行的
# l3 = [i for i in l2]
print("*" * 20)

# 这里为空是因为上面第13行，已使用for语句进行了迭代，而迭代器迭代了一次后
# 就为空了？（为空还是指向末尾？）
l3 = list(l2)
print(l3)

print("*" * 20)
l4 = map(mulTen, l1)
print(list(l4))