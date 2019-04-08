# coding = utf-8
import rediscluster.client

startup_nodes = [
    {"host": "192.168.31.140", "port": 6379},
    {"host": "192.168.31.140", "port": 6380},
    {"host": "192.168.31.140", "port": 6381},
    {"host": "192.168.31.140", "port": 6382},
    {"host": "192.168.31.140", "port": 6383},
    {"host": "192.168.31.140", "port": 6384}
]
cluster_conn = rediscluster.client.RedisCluster(startup_nodes=startup_nodes)
str_data = cluster_conn.get('py_user')
print(str_data)
