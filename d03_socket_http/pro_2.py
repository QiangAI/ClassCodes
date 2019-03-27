# coding=utf-8
import os

pipe_file = 'io.pipe'
os.mkfifo(pipe_file)

fd = os.open(pipe_file, os.O_RDONLY)
while True:
    s = os.read(fd, 10)
    if not s:
        break
    print(s.decode())
