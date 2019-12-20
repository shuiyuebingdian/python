'''
正整数的反转
例如：将12345变成54321
'''

# 输入要反转的正整数
Num = int(input("请输入："))

while Num > 0:
    print(Num % 10, end="")
    Num = Num // 10

