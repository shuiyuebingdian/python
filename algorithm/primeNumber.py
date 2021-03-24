"""
打印100以内的质数
质数（Prime number），又称素数，
指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数

思路：
循环比这个数的平方根还小的数，并取模，都不能整除，就是素数了
"""
arr=[]
for i in range(1, 101):
    j=2
    isPrime=True
    while j*j<=i:
        if i%j==0:
            isPrime=False
            break
        j=j+1
    if (isPrime):
        arr.append(i)

#print(arr)
        

"""
python官网示例
"""

for n in range(2, 101):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print(n, "is a prime number")
