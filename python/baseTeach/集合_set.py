# 集合

# add()：添加集合元素
s1 = set()
s1.add('alex')
print(s1)   # {'alex'}
s1.add('alex')
print(s1)   # {'alex'}

# difference()：返回当前集合和传入集合的不同 / difference_update()：更新当前集合
s2 = set(['alex', 'eric', 'tom', 'alex'])
print(s2)   # {'tom', 'alex', 'eric'}
s3 = s2.difference(['alex', 'eric'])
print(s3)   # {'tom'}
s2.difference_update(['alex', 'eric'])
print(s2)   # {'tom'}

# pop()取走一个元素
s2 = set(['alex', 'eric', 'tom', 'alex'])
ret = s2.pop()
print(ret)  # alex/eric/tom






