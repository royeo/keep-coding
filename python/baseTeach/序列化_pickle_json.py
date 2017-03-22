# 序列化
# pickle和json相比，pickle可以序列化的场景更多
import pickle, json

# 将对象序列化
print('pickle.dumps()将对象序列化：')
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

# pickle.dump()直接把对象序列化后写入一个file
with open("user_acc.txt", "wb") as f:
    pickle.dump(d, f)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后就可以把这个bytes写入文件
with open("user_acc.txt", "ab") as f:
    f.write(pickle.dumps(d))

# pickle.load()方法从一个file-like Object中直接反序列化出对象
with open("user_acc.txt", "rb") as f:
    print('\npickle.load()方法：')
    print(pickle.load(f))

# pickle.loads():先从文件中读出来，然后通过pickle.loads()序列化
with open("user_acc.txt", "rb") as f:
    print('\npickle.loads()方法：')
    print(pickle.loads(f.read()))

# 将对象序列化
print('\njson.dumps()将对象序列化：')
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

# 将对象反序列化
print('\njson.loads()将对象反序列化：')
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

# json进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)
print('\n将类实例转化为JSON：')
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

print('\n将JSON转化为类实例：')
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))









