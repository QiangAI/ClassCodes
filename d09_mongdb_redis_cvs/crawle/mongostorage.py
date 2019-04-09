import pymongo
"""
    MongoDB的数据存储

"""


class MongoDBStorage:

    def __init__(self):
        # 定义服务器数据(参数传递，或者配置文件ini，xml，json，csv)
        self.__host = '127.0.0.1'
        self.__port = 9988
        # self.__user = ''
        # self.__password = ''
        # 直接链接
        self.__client = pymongo.MongoClient(host=self.__host, port=self.__port)
        self.__db = self.__client.lagou
        self.__collection = self.__db.jobs

    def add_rows(self, rows):
        """
        添加数据到MongoDB
        :param rows: 数据文档集
        :return:
        """
        print('开始存储数据')
        for row in rows:
            self.__collection.insert_one(row)

    def close(self):
        print('存储关闭')
        self.__client.close()
