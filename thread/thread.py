'''
import time,threading
def loop():
    print('thread {0} is running ...'.format(threading.current_thread().name))
    n = 0
    while n<5:
        n = n+1
        print('thread {0} >>> {1}'.format(threading.current_thread().name,n))
        time.sleep(1)
    print('thread {0} ended.'.format(threading.current_thread().name))

print('thread {0} is running...'.format(threading.current_thread().name))
t= threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread {0} ended'.format(threading.current_thread().name))
'''

'''
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''

import threading
local_school=threading.local()
def process_student():
    std=local_school.student
    print('Hello,{0} (in {1})'.format(std,threading.current_thread().name))
def process_thread(name):
    local_school.student  = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()