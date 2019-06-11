# 启动docker容器
docker run -itd -p 6379:6379 -v ${PWD}/data:/data redis:2019.06 redis-server /etc/redis.conf --appendonly yes 

# -it 交互模式
# -d 后台启动
# -p 映射宿主机端口：容器端口
# -v 挂载宿主机目录：容器目录