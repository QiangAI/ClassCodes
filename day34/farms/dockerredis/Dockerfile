# 基础镜像
FROM redis

# 镜像维护者
MAINTAINER Louis Young

# 拷贝本地的Redis配置文件到容器内
COPY ./redis.conf  /etc/

# 映射端口，在docker命令中使用-p指定宿主端口与容器端口映射（-p 宿主端口：容器端口）
EXPOSE 6379

# 挂载外部目录（自动挂载非指定目录），在docker命令中使用-v选项挂载指定宿主目录与容器目录（-v 宿主目录：容器目录）
# VOLUME ["/data",]

# 启动Redis服务器(也可以使用docker启动服务器，docker启动更加灵活)
# CMD ["redis-server",]
