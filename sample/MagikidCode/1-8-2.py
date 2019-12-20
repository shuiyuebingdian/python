'''
1-8-2
数据结构（列表List）
List是一种有序的集合，可以随时添加和删除其中的元素

List中的元素可以是不同的数据类型

len()函数可以获得List元素的个数

append()函数可以往List中追加元素到末尾
'''

# 定义一个空列表
Classmates = []
print("定义一个空列表: Classmates = []")

# 此时Classmates的个数是0
ClassmatesLength = len(Classmates)
print("此时Classmates的个数是: " + str(ClassmatesLength))

# 用append()函数往Classmates中添加元素
Classmate1 = "李潇艺"
Classmates.append(Classmate1)
print("往Classmates中添加元素: " + Classmate1)

# 此时Classmates的个数是1
ClassmatesLength = len(Classmates)
print("此时Classmates的个数是: " + str(ClassmatesLength))

Classmate2 = "谭高阳"
Classmates.append(Classmate2)
print("往Classmates中添加元素: " + Classmate2)

# 此时Classmates的个数是2
ClassmatesLength = len(Classmates)
print("此时Classmates的个数是: " + str(ClassmatesLength))

# 打印列表Classmates
print(Classmates)

# 用索引访问列表的元素
for i in range(ClassmatesLength):
    print("Classmates[" + str(i) + "]: " + Classmates[i])

# 打印空行
print()

# 定义一个包含多种数据类型元素的列表
List = ["语文", "香蕉", 344, True, 283.4]
Length = len(List)
for i in range(Length):
    print("List[" + str(i) + "]: " + List[i])
