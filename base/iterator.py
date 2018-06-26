# from collections import Iterable

# print(isinstance('abc',Iterable))
# print(isinstance([1,2,3],Iterable))
# print(isinstance(123,Iterable))

# for i,value in enumerate(['A','B','C']):
#     print(i,value)

def findMinAndMax(L):
    max = None
    min = None
    for i in L:
        if max == None:
            max = i
        elif i > max :
            max = i
        if min == None:
            min = i
        elif i < min:
            min = i
    return(min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')