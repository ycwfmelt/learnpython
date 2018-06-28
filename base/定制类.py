class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L


for n in Fib():
    print(n)
f = Fib()
print(f[46])
print(f[0:10])


class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('{0}/{1}'.format(self.__path, path))

    def __str__(self):
        return self.__path
    __repr__ = __str__


print(Chain().status.user.timeline.list)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is {0}'.format(self.name))


s = Student('Michael')
s()
