
def bubble_sort(data):
    """冒泡排序"""
    # 数据长度做为循环次数
    for j in range(len(data)+1):
        # 两两之间进行比较大小，挑选出最大数
        for i in range(len(data)-(j+1)):
            if data[i] > data[i+1]:
                # 定义一个变量来存储某一数据
                tmp = data[i+1]
                data[i+1] = data[i]
                data[i] = tmp
    print(data)
