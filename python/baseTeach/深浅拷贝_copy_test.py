# 深拷贝/浅拷贝
import copy
a = 123
b = 123
print('a = 123, &a =', id(a))
print('b = 123, &b =', id(b))

c = a
print('c = a, &c =', id(c))
d = copy.copy(a)
print('d = copy.copy(a), &d =', id(d))
e = copy.deepcopy(a)
print('e = copy.deepcopy(a), &e =', id(e))

# 应用
dic = {
    'cpu': [80, ],
    'mem': [80, ],
    'disk': [80, ]
}
print('before: ', dic)
# new_dic = copy.copy(dic)
new_dic = copy.deepcopy(dic)
new_dic['cpu'][0] = 50
print(dic)
print(new_dic)
