L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[]
for i in L1:
    if isinstance(i,str):
        L2.append(i.lower())
    elif i == None:
        pass
    else:
        pass

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')