# 面向对象高级特性
class Student:
    pass


# 给实例绑定方法
print('__给实例绑定方法__')
def set_age(self, age):
    self.age = age

s = Student()
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print('s.age = ', s.age)


# 给class绑定方法
print('\n__给class绑定方法__')
def set_score(self, score):
    self.score = score

Student.set_score = set_score
h = Student()
h.set_score(100)
print('h.score = ', h.score)


# 使用__slots__，限制实例的属性(只对当前类实例起作用，对继承的子类是不起作用的)
print('\n____slots____')
class Teacher(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Teacher()
s.name = 'jack'
s.age = 12
# s.score = 99  # 报错

# @property装饰器：负责把一个方法变成属性调用
print('\n__@property__')
class Boy(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100!')
        self._score = value

b = Boy()
b.score = 60
print('b.score = ', b.score)
# b.score = 999   # 报错


# __iter__：迭代对象
print('\n__iter__')
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)


# __getitem__：像list一样按照下标取出元素
print('\n__getitem__')
class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

f = Fib()
print(f[0], f[1], f[2], f[3], f[4])

# __getattr__：获取属性
print('\n__getattr__')
class Txt(object):
    def __init__(self):
        self.name = 'jack'

    def __getattr__(self, item):
        if item == 'score':
            return 99

t = Txt()
print(t.name)
print(t.score)


# __call__：直接对实例进行调用
print('\n__call__')
class Vim(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('name is %s.' % self.name)

v = Vim('jack')
v()








