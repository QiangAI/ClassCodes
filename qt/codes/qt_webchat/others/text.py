import sys

import itchat
from PyQt5.QtWidgets import *
from apscheduler.schedulers.qt import QtScheduler

itchat.auto_login(hotReload=False)
chat_rooms = itchat.get_chatrooms()


def SentChatRoomsMsg(name, context):
    f = itchat.search_friends(name='沈姐姐')
    r = itchat.send_msg('大家好', f[0]['UserName'])
    print(r)


app = QApplication([])
w1 = QWidget()
w2 = QWidget()
w1.show()
w2.show()
scheduler = QtScheduler()
scheduler.start()
scheduler.add_job(SentChatRoomsMsg,
                  kwargs={"name": 'oooo', "context": 'kkkkk'})

print('结束')
code = app.exec()
sys.exit(code)
