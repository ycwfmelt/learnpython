import time
import sys
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 链接到服务器
server_addr = '127.0.0.1'
print('Connect to server {0}...'.format(server_addr))

m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task {0} * {1}'.format(n,n))
        r = '{0} * {1} = {2}'.format(n,n,n*n)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('work exit.')
