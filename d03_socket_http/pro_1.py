# coding=utf-8
import os
import time

pipe_file = 'io.pipe'
fd = os.open(pipe_file, os.O_SYNC | os.O_CREAT | os.O_RDWR)
for i in range(10):
    os.write(fd, ('%d' % i).encode())
    # s = os.read(fd,10)
    # print(s.decode())
    time.sleep(1)

os.unlink(pipe_file)
