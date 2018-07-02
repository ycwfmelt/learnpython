'''
import pickle

d = dict(name='Bob', age=20, score=99)

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as g:
    print(pickle.load(g))
'''

'''
import json

json_str = '{"age":20,"score":99,"name":"Bob"}'
print(json.loads(json_str))
'''


import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return{
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 89)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age":20,"score":99,"name":"Bob"}'

print(json.loads(json_str,object_hook=dict2student))