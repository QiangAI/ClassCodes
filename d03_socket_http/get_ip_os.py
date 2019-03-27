# coding=utf-8
import subprocess

prop = subprocess.Popen(['ifconfig', 'en0'], stdout=subprocess.PIPE)
# prop = subprocess.Popen(['networksetup',
#                          '-setmanual',
#                          'Wi-Fi',
#                          '192.168.1.88',
#                          '255.255.255.0',
#                          '192.168.1.1'],stdout=subprocess.PIPE)
while True:
    line = prop.stdout.readline()
    if not line:
        break
    print(":", line.decode(), end='')

if prop.poll() is None:
    print("该程序在运行")
if prop.poll() > 0:
    print("程序错误退出")
if prop.poll() == 0:
    print("该程序正常退出")
if prop.poll() < 0:
    print("该程序被kill杀死")
