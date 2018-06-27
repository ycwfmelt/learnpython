from functools import reduce

def normalize(name):
    return name[:1].upper()+name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x,y:x*y,map(int,L))
# 测试：
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# def str2float(s):
#     s1 = s.split('.')
#     return reduce(lambda x,y:x*10+y,map(c2n,s1[0]))+reduce(lambda x,y:x+y/10,map(c2n,s1[1]))/10






def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

def mae(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

def ushiro(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))/pow(10,len(s))

def str2float(s):
    ss = s.split('.')
    return mae(ss[0])+ushiro(ss[1])
    
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')