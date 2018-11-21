# 排序案例

# 倒序
a = [23,56,3,4,5,64,31,34,543,1]

al = sorted(a, reverse=True)
print(al)


#绝对值倒序
print("*"*20)

a2 = [-43,55,-95,-6,2,568,-98,]
al2 = sorted(a2, key = abs, reverse=True)
print(al2)

# 字符串

astr = ['fas', 'Dadt', 'Tdkg','jlti']

str1 = sorted(astr)
print(str1)

print(str.lower)
# key=str.lower 这里传入的是str的lower方法，
# 将astr中的值全转换为小写进行排序
# 参数key用来接收函数
str2 = sorted(astr, key=str.lower)
print(str2)

