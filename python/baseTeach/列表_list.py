# 列表
name_list = ['brother', 'alex', 'single', 'xman', 'yes']
print(name_list)
print(name_list[0], name_list[1], name_list[2])

# 切片(顾首不顾尾)
print('1. ', name_list[-1])
print('2. ', name_list[-2:])
print('3. ', name_list[:2])
print('4. ', name_list[1:3])
print('5. ', name_list[0:5:2])

# 追加
name_list.append('copy')
print('append(): ', name_list)

# index只能找到第一个
print('index(): ', name_list.index('copy'))

# 计算列表里有多少个元素
print('count(): ', name_list.count('copy'))

# 插入
name_list.insert(2, 'second')
print('insert(): ', name_list)

# 删除
name_list.remove('second')
print('remove(): ', name_list)

# 排序
name_list.sort()
print('sort(): ', name_list)

# 删除列表里所有的copy元素
name_list.append('copy')
for i in range(name_list.count('copy')):
    name_list.remove('copy')
print('remove all copy: ', name_list)

# 扩展
name_list.extend(['extend', 'kady'])
print('extend(): ', name_list)







