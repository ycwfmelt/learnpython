from types import MethodType


class Student(object):
    __slots__=('name','age')


s = Student()
s.name = 'Michael'
print(s.name)


# def set_age(self, age):
#     self.age = age


# s.set_age = MethodType(set_age, s)
# s.set_age(25)



# def get_age(self):
#     return self.age


# Student.get_age = get_age

# print(s.get_age())

class Gs(Student):
    __slots__=('s')

g=Gs()
g.name = 'asd'
print(g.name)

