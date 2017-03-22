from datetime import datetime
now = datetime.now()
print('获取当前日期和时间')
print(now)
print(type(now))

print('\n指定日期时间创建datetime')
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

print('\ndatetime转换为timestamp')
dt = datetime(2015, 4, 19, 12, 20)
print(dt.timestamp())

print('\ntimestamp转换为datetime')
t = 1429417200.0
print(datetime.fromtimestamp(t))


print('\ntimestamp转换为UTC时间')
t = 1429417200.0
print(datetime.utcfromtimestamp(t)) # UTC时间

print('\n字符串转datetime')
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print('\ndatetime转字符串')
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

