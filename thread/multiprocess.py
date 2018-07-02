''' unix like
import os

print('Process ({0}) start ...'.format(os.getpid))

pid = os.fork()

if pid == 0:
    print('I am child process')
else:
    print('I just created a child process')
'''


'''
from multiprocessing import Process
import os

# subProcess code to exec
def run_proc(name):
    print('Run child process {0}({1})'.format(name,os.getpid()))

if __name__ == '__main__':
    print('Parent process {0}'.format(os.getpid()))
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end')
'''


import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.baidu.com'])
print('Exit code:',r)