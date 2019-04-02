class myfile(object):
    def __init__(self, filename):
        self.__file = filename

    def __enter__(self):
        print('代码执行到了__enter__......')
        # 打开文件
        self.__fd = open(self.__file, 'w')

        def write_(content):
            self.__fd.write(content)

        self.write_content = write_
        return self

    # 退出方法中，用来实现善后处理工作
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('代码执行到了__exit__......')
        self.__fd.close()


# a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
with myfile('test.txt') as f:
    # 创建写入文件
    f.write_content('hello')
