# 操作文件和目录
import os
print(os.name)  # posix代表Linux、Unix、MacOS; nt表示window

print('获取详细信息:\n', os.uname())

print('查看环境变量：\n', os.environ)

print('获取某个环境变量的值:\n', os.environ.get('PATH'))

print('查看当前目录的绝对路径:\n', os.path.abspath('.'))
print('在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:\n', os.path.join('/home/ljn/WorkSpace/BaseTeach', 'testdir'))
# print('创建一个目录:\n', os.mkdir('/home/ljn/WorkSpace/BaseTeach/testdir'))
# print('删掉一个目录:\n', os.rmdir('/home/ljn/WorkSpace/BaseTeach/testdir'))

print('拆分路径:\n', os.path.split('/home/ljn/WorkSpace/BaseTeach/testdir'))

print('得到文件扩展名:\n', os.path.splitext('/path/to/file.txt'))

# print('对文件重命名:\n', os.rename('test.txt', 'test.py'))

# print('删除文件:\n', os.remove('test.py'))

print('列出当前目录下的所有目录:\n', [x for x in os.listdir('.') if os.path.isdir(x)])

print('列出当前目录下的所有文件:\n', [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
