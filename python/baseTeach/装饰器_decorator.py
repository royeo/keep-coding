# 装饰器
def w1(main_func):
    def outer(arg):
        print('before')
        main_func(arg)
        print('after')
    return outer


@w1
def show(arg):
    print('this is [%s]' % arg)

# @w1
#   执行w1,把自己装饰的函数的函数名当作参数,w1(show)
#   show函数重新定义, show = w1(show)
show('alex')


# 可以传多个参数的装饰器
def before():
    print('before')


def after():
    print('after')


def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(args):
            before_func()
            main_func(args)
            after_func()
        return wrapper
    return outer


@Filter(before, after)
def bill(name):
    print('bill is [%s]' % name)

bill('alex')
