try:
    f = open("c:/Users/dell/Documents/GitHub/learnpython/io/file.txt","r")
    print(f.read())
    f.close
finally:
    if f:
        f.close()

with open("c:/Users/dell/Documents/GitHub/learnpython/io/file.txt","r") as f:
    print(f.read())

#在内存中读写str
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

from io import StringIO
f=StringIO("hello!\nHi!\nGoodbye!")
while True:
    s=f.readline()
    if s =='':
        break
    print(s.strip())

# 操作二进制数
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))