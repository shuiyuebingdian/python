'''
1-7-3: 变量的命名规则
1）变量名由字母、数字和下划线组成，不能以数字开头
2）大小写敏感（大写的A和小写的a是两个不同的变量）
3）不要跟关键字和系统保留字冲突

最好采用：
1）驼峰式命名，如lasName, firstName
2）用下划线连接，如last_name, first_name
'''

# 定义两个姓名的变量
FirstName = input("请输入你的第一个名字：")
LastName = input("请输入你的第二个名字：")

# 打印变量name的值
print("你的全名叫：", FirstName, LastName)
