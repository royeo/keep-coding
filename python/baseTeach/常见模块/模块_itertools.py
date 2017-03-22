# itertools提供了非常有用的用于操作迭代对象的函数
import itertools

# 无限迭代
# natuals = itertools.count(1)
# natuals = itertools.cycle('ABC')
# natuals = itertools.repeat('A', 3)
# for n in natuals:
#     print(n)

# 通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
print('\n__chain()__')
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
print('\n__groupby()__')
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))


