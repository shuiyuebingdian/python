'''
 1-8-3_The_value_in_the_list 访问列表中的值
 列表是有序的，列表中的每一个数据项(元素)都有自带的位置信息，称之为“索引”。
 列表的“索引”从 0 开始。
'''

# 声明一个string(字符串)变量，变量名为name，并给变量name赋值为李潇艺
name = "李潇艺"

# 声明一个int(整数型)变量，变量名为age，并给变量age赋值为10
age = 10

# 声明一个float(浮点型)变量，变量名为weigh(体重Kg)，并给变量weigh赋值为49.6
weigh = 49.6

# 声明一个boolean(布尔型)变量，变量名为handsome，并给变量handsome赋值为True
handsome = True


print("我叫" + name + "，今年" + str(age) + "岁，体重"
      + str(weigh) + "Kg")
if handsome:
    print("我很帅！")

print()


# 声明一个list变量，变量名为list1，并给变量list1赋值
list1 = [1, 2, 3, 4, 5]
# 访问 list1 中第3个数据项(元素)
print("list1[2]: ", list1[2])

# 声明一个list变量，变量名为list2，并给变量list2赋值
list2 = ["a", "b", "c", "d", "e"]
# 访问 list2 中第2到第4个数据项(元素)
print("list2[1:4]: ", list2[1:4])

# 声明一个list变量，变量名为list3，并给变量list3赋值
list3 = ["Thanksgiving", "Halloween", "Christmas"]
# 访问 list3 中最后一个数据项(元素)
print("list3[-1]: ", list3[-1])

# 声明一个list变量，变量名为list4，并给变量list4赋值
list4 = [True, False]
# 访问 list4 中倒数第二个数据项(元素)
print("list4[-2]: ", list4[-2])

# 声明一个list变量，变量名为list5，并给变量list5赋值
list5 = [1, "a", "Thanksgiving", False, "b", "c", 4, 5]
# 访问 list5 中第2到第6个数据项(元素)
print("list5[1:6]: ", list5[1:6])
    
 

 

 

 

 

