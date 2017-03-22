# 生成器
# 定义：一个函数调用时返回一个迭代器，那么这个函数就叫做生成器
#      如果函数中有yield,那么这个函数会变成生成器


def cash_money(amount):
    while amount > 0:
        amount -= 100
        yield 100
        print('又来取钱了!, 还剩', amount)

atm = cash_money(500)
print(atm)
print(atm.__next__())
print(atm.__next__())
print("叫个大保健...")
print(atm.__next__())
print(atm.__next__())
print(atm.__next__())


