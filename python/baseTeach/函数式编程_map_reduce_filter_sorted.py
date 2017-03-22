# map迭代
def f(x):
    return x * x

r = map(f, list(range(1, 10)))
print('[map]：', list(r))

h = map(f, set(range(1, 10)))
print('[map]：', set(h))

k = map(str, list(range(1, 10)))
print('[map]：', list(k))

# reduce：把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, ...] = f(f(f(x1, x2), x3), x4))
from functools import reduce
m = reduce(lambda x, y: x + y, [1, 3, 5, 7, 9])
print('[reduce]：', m)

# filter:把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
print('[filter]：', list(filter(lambda x: x % 2 == 1, list(range(1, 10)))))

# sorted:排序
print('[sorted]：', sorted([36, 5, 19, -3, 2]))
print('[sorted]：', sorted([36, 5, 19, -3, 2], key=abs))