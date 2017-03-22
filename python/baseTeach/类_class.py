# 类
print('\n___类___')
class Student(object):
    num = '9527'

    def __init__(self, name, score, address):
        self.name = name
        self.score = score
        self.__address = address    # 实例的变量名如果以__开头，就变成了一个私有变量

    def print_score(self):
        print('%s:%s' % (self.name, self.score))

bart = Student('Bart', 59, '黄埔')
lisa = Student('Lisa', 87, '天河')
bart.print_score()
lisa.print_score()
print(Student.num)
print(bart.num)
bart.num = '9999'
print(bart.num)
print(Student.num)

lisa.age = 11       # 可以自由的绑定属性
print(lisa.age)

print(hasattr(bart, 'name'))
print(getattr(bart, 'name'))
setattr(bart, 'name', 'Dart')
print(getattr(bart, 'name'))
print(getattr(bart, 'age', 404))    # 设置默认值



# 继承
print('\n___继承___')
class Animal(object):
    def run(self):
        print('Animal is running')

class Runnable(object):
    def run(self):
        print('Running...')

class Dog(Animal, Runnable):
    pass

class Cat(Animal, Runnable):
    pass

dog = Dog()
cat = Cat()
dog.run()
cat.run()


# isinstance判断class的类型
print('\n___isinstance___')
print(isinstance(dog, Dog))
print(isinstance([1, 2, 3], (list, tuple)))

# type：判断对象类型
print('\n___type___')
import types

def fn():
    pass

print(type(123))
print(type(abs))
print(type(123) == int)
print(type(fn) == types.FunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        print('SchoolMember [%s] is enrolled' % self.name)


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, course, salary):  # sda
        super(Teacher, self).__init__(name, age, sex)
        self.course = course
        self.salary = salary

    def teaching(self):
        print('Teacher [%s] is teaching' % self.name)


class Student(SchoolMember):
    def __init__(self, name, age, sex, course, tuition):
        super(Student, self).__init__(name, age, sex)
        self.course = course
        self.tuition = tuition

    def pay_tuition(self):
        print('')




