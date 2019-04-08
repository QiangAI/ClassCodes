# coding = utf-8
import time

import redis.connection

r = redis.client.Redis(host='127.0.0.1', port=6379, db=0, password='yq123456')


def my_cb(pipe_):
    pipe_.multi()
    pipe_.set(name='py_user', value='Jack-Hello')
    print("睡眠")
    time.sleep(5)
    pipe_.set(name='linux_user', value='root')
    if pipe_.execute():
        print("提交成功")
    else:
        print("提交失败")


r.transaction(my_cb, 'py_user')
