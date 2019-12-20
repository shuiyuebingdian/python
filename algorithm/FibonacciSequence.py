"""
斐波那契数列由0和1开始，之后的斐波那契数就是由之前的两数相加而得出
"""


def fbnq(num):
    """
    列出num位个斐波那契数列
    """
    arr=[]
    a, b = 0, 1
    for i in range(num):
        arr.append(a)
        a, b = b, a + b
    
    print(arr)
        
print("10位斐波那契数列")
fbnq(10)
print()


def fbnq_item(num):
    """
    列出斐波那契数列的第num位个数是几
    """
    a, b = 0, 1
    for i in range(num - 1):
        a, b = b, a + b
    return a
print("第10位斐波那契数列元素")
print(fbnq_item(10))
print()


"""
官网示例
"""
def fbnq_from_offical_website(num):
    a, b = 0, 1
    while a < num:
        print(a, end=",")
        a, b = b, a + b
        

print("从0开始，小于10的斐波那契数列")
fbnq_from_offical_website(10)
print()

def fbnq_from_offical_website(num):
    a, b = 0, 1
    while num > 0:
        print(a, end=",")
        a, b = b, a + b
        num = num - 1
        

print("\n从0开始，10位的斐波那契数列")
fbnq_from_offical_website(10)
