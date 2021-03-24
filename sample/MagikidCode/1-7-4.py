'''
1-7-4: 变量的使用
使用变量保存数据并进行算术运算,
使用type()函数对变量的类型进行检查
'''

# 定义一个整型变量
a = 1

# 打印10加变量a的结果
print("10 + " + str(a) + " =" + str(10 + a))

# 定义一个浮点型变量
b = 12.32
# 定义一个变量保存10加变量b的结果
Sum = 10 + b
# 打印Sum的值
print("10 + " + str(b) + " =" + str(Sum))
# 打印Sum的类型
print("Sum的类型是：" + str(type(Sum)))

# 定义一个字符串变量
c = "hello, world"
# 打印c的值
print("c = " + c)
# 打印c的类型
print("c的类型是：" + str(type(c)))

# 定义一个布尔型变量
d = True
# 打印d的值
print("d = " + str(d))
# 打印d的类型
print("d的类型是：" + str(type(d)))
