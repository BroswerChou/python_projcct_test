# # coding=utf-8
#
# # 第一行注释一般有特殊用法
# # 字符串  字符串用单引号、双引号、三单引号（可以换行）、三双引号
# print("I'm a teacher")
# a = "你很好"
# print(a)
# # r表示让转义失效
# a = "123""456 "    # 隐式拼接
# b = a*2
# c = a + b
# print(a, '\n', b, '\n', c)
#
# # 切片访问
# d = a[2:5]
# e = a[5:2:-1]
# print(d)
# print(e)
# g='abcd'
# print(g.title())


# # 新建一个列表，包含前十个整数的平方
#
# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)
# print(max(squares))
# print(min(squares))
# print(sum(squares))
#
# # 列表解析
# squares1 = [value**2 for value in range(1,12)]
# print(squares1)


# # 打印1-20的奇数
# list1 = []
# for value in range(1,20,2):
#     list1.append(value)
# print(list1)
# list_copy = list1[:] # 使用切片是创建了一个新的列表
# print(list_copy)
# list1.append(20)
# print(list1)
# print(list_copy)
# list_dri_copy = list1 # 不使用切片，直接赋值是指向同一个
# print('list1:',list1)
# print('list_copy:',list_copy)
# print('list_dri_copy:',list_dri_copy)

# # 元组
# dimensions = (200, 50,20,96,56) # 如果要修改元组，应该重新定义
# print(dimensions[0])
# for dimension in dimensions:   # 遍历元组
#     print(dimension)

# # if 语句
# cars = ['audi','bwn','subaru','toyo']
# if 'audi' not in cars:
#     print('1')
# else:
#     print('0')
# for car in cars:
#     if car != 'bwn':
#         print(car.upper())
#     else:
#         print(car)
# # 外星人染色
# alien_color='red'
# number=0
# if alien_color == 'green':
#     number=5
# elif alien_color == 'yellow':
#     number=10
# else:
#     number=15
# print("获得"+str(number)+"个点")

# 处理列表
users=['wangkai','liling','admin','zhouyi','zhayue']
if users:
    for user in users:
        if user == 'admin':
            print("hello " + user + " ,would you like to see a status repot")
        else:
            print(user + ",welcome to china")
else:
    print("None")



