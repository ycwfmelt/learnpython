import functools
int2=functools.partial(int,base=2)
n = int2('10000')
print(n)