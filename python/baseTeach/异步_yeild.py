# 异步
import time

def consumer(name):
    print("%s 准备吃包子啦" % name)
    while True:
        baozi = yield
        print("包子[%s]来啦,被[%s]吃了！" % (baozi, name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('老子开始做包子了')
    for i in range(3):
        time.sleep(1)
        print("做了2个包子")
        c.send(i)
        c2.send(i)

producer('Alex')