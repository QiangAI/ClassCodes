# coding=utf-8
import os

a = 20
pid = os.fork()
if pid == 0:
    while True:
        print('子进程', pid, a)
else:
    a = 888
    while True:
        print('父进程', pid, a)
