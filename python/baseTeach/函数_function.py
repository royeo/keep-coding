    # 加一个星会自动转化为元祖
# def show(*arg):
#     print(arg, type(arg))
#
# show(1, 2, 3, 4)


# 加两个星会自动转化为字典
# def show1(**arg):
#     print(arg, type(arg))
#
# show1(n1=78, n2='a', n3='bbb')


# def show2(*arg, **kwargs):
#     print(arg, type(arg))
#     print(kwargs, type(kwargs))
#
# show2(11, 22, 33, 44, n1=88, n2='xx')
# a = [11, 22, 33, 44]
# b = {'n1': 88, 'n2': 'xx'}
# # show2(a, b)   #a,b都赋值给arg,kwargs为空
# show2(*a, **b)


# s1 = "{0} is {1}"
# l = ['alex', 'sb']
# print(s1.format('alex', 'sb'))
# print(s1.format(*l))


s2 = "{name} is {acter}"
k = {'name': 'alex', 'acter': 'sb'}
print(s2.format(name='alex', acter='sb'))
print(s2.format(**k))
