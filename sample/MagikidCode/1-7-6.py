'''
猜数字游戏
计算机生成一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示：大了/小了/猜对了,
并记录猜了几次
'''

import random

# 生成一个随机的整数型数字,数字范围在1~100
answer = random.randint(1, 100)

# 猜的次数，初始为0，猜一次加1
counter = 0

while True:
    num = int(input("请输入："))
    counter = counter + 1
    if num > answer:
        print("大了")
    elif num < answer:
        print("小了")
    else:
        print("对了")
        break;

print("你总共猜了" + str(counter) + "次")
    
