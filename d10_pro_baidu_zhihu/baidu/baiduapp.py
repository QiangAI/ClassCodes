import baidu.baiducrawler
import baidu.baidudialog

"""

    功能：组合百度翻译的UI与百度翻译爬虫模块，形成完整的翻译业务流程
    作者：Louis Young
    日期：2019-04-10
"""


class BaiduApp:

    def __init__(self):
        self.__crawler = baidu.baiducrawler.BaiduCrawler()
        self.__dlg = baidu.baidudialog.BaiduDialog(self.__crawler)

    def start(self):
        print('开始应用')
        self.__dlg.show()
