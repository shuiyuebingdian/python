'''
打印三角形图案
    *
   **
  ***
 ****
*****

第一行打印4个空白符1个星星符
第二行打印3个空白符2个星星符
第三行打印2个空白符3个星星符
第四行打印1个空白符4个星星符
第五行打印0个空白符5个星星符
'''


# 星星符号
star = "*"

# 空白符号
space = " "

# 输入打印行数
num = int(input("请输入行数:"))

'''
方式一：
'''
for i in range(num):
    # 打印的空白符号的个数
    spaceNum = num - i - 1
    
    print(spaceNum * space + (i + 1) * star)


'''
方式二：

for i in range(num):
    # 打印的空白符,不换行
    for j in range(num - i - 1):
        print(space, end="")

    # 打印星星,不换行
    for h in range(i + 1):
        print(star, end="")

    # 打印换行
    print()
'''
