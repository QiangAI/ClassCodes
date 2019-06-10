# 基础镜像
FROM python

# 镜像维护者
MAINTAINER Louis Young

# 工作目录
RUN cd /home
RUN mkdir mycodes

WORKDIR /home/mycodes

# 拷贝安装列表文件，执行python模块安装
COPY pythonlist.txt ./
# 更新pip最新安装
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r pythonlist.txt

# 拷贝项目文件，执行项目
copy recurit.py ./
CMD [ "python", "./recurit.py" ]
