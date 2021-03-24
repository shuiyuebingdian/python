'''
打印三角形图案
*
**
***
****
*****
'''

star = "*"

# 输入打印行数
num = int(input("请输入行数:"))

'''
方式一：
for i in range(1, num + 1):
    print(i * star)
'''

'''
方式二：
'''
for i in range(num):

    # 打印星星,不换行
    for h in range(i + 1):
        print(star, end="")

    # 打印换行
    print()
