# 文件操作

# 写操作
def writefile():
    f = open('test.log', 'w')
    f.write('this is 1\n')
    f.write('this is 2\n')
    f.close()

# 读操作
def readfile():
    f = open('test.log', 'r')
    for line in f:
        if '1' in line:
            print("this is first line")
    f.close()

# 追加
def appendfile():
    f = open('test.log', 'a')
    f.write('this is 3\n')
    f.close()

# 可读写(一般不用这种模式)
def readwritefile():
    f = open('test.log', 'w+')
    f.write('this is 4')
    print(f.readline())
    f.close()

readfile()
