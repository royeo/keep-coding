# 迭代器
names = iter(['alex', 'java', 'php'])
print(names)
print(names.__next__())
print(names.__next__())
print(names.__next__())

# 实例
# 这就是一个python已经实现的迭代
f = open('__init.py')
for line in f:
    print(line)
