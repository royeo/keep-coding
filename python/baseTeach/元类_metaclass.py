# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，
# 仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
def fn(self, name='world'):
    print('hello %s' % name)

# 要创建一个class对象，type()函数依次传入3个参数：
# 1、class的名称；
# 2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()


# metaclass（元类）：允许你创建类或修改类，可以把类看作是metaclass创建出来的实例
class ListMetaclass(type):  # metaclass是类的模板，所以必须从`type`类型派生
    def __new__(typ, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(typ, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)



