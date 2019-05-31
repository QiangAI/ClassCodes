import tensorflow  as tf
import tensorflow.train  as tr
from sklearn import datasets

'''
'''
alpha = 1

INPUT_SIZE = 4
OUTPUT_SIZE = 1
# 我们使用鸢尾花数据作为分类测试

# 1. 定义数据（一般是样本与样本标签）
x = tf.placeholder(dtype=tf.float32, shape=[None, INPUT_SIZE])
y = tf.placeholder(dtype=tf.float32, shape=[None, OUTPUT_SIZE])
init_w = tf.random_uniform(shape=(INPUT_SIZE, OUTPUT_SIZE), minval=-0.1, maxval=0.1, dtype=tf.float32)
init_b = tf.random_uniform(shape=[OUTPUT_SIZE], minval=-0.1, maxval=0.1, dtype=tf.float32)
w = tf.Variable(init_w)
b = tf.Variable(init_b)

# 2. 决策参数模型描述
o_y = tf.add(tf.matmul(x, w), b)

o_predict = tf.sign(o_y)
# Declare vector L2 'norm' function squared
l2_norm = tf.reduce_sum(tf.square(w))

# Loss = max(0, 1-pred*actual) + alpha * L2_norm(A)^2
alpha = 0.01
hinge = tf.losses.hinge_loss(y, o_y)  # tf.reduce_mean(tf.maximum(0., tf.subtract(1., tf.multiply(o_y,  y))))
# loss = tf.add(l2_norm, tf.multiply(alpha, hinge))
loss = hinge + alpha * l2_norm

optimizer = tr.GradientDescentOptimizer(learning_rate=0.01)
# optimizer = tf.train.RMSPropOptimizer(learning_rate=0.01)
trainer = optimizer.minimize(loss=loss)
# --------------------------------- 静态图
graph_writer = tf.summary.FileWriter("./graphs", graph=tf.get_default_graph())
graph_writer.flush()
graph_writer.close()
# ---------------------------------
# 4. tensorflow运算执行会话环境
op_init = tf.initializers.global_variables()
session = tf.Session()
session.run(op_init)
# 5. 执行与训练
data, target = datasets.load_iris(return_X_y=True)
data = data[50:150]
target = target[0:100]
target[target == 0] = -1  # -1 与 1

target = target.reshape(target.shape[0], OUTPUT_SIZE)

# 训练次数
# 分epoch，每个epoch分若干batch，每个batch若干样本
epoch = 10000
batch_size = 10
batch_num = 10
for t in range(epoch):
    for i in range(batch_num):
        session.run(trainer, feed_dict={x: data[i * batch_size:(i + 1) * batch_size],
                                        y: target[i * batch_size:(i + 1) * batch_size]})
    ls = session.run(loss, feed_dict={x: data, y: target})
    # print(ls)
    if ls < 10e-5:
        print("梯度过小，结束训练！")
        break
# 6. 预测与分类评估
o_v = session.run(o_predict, feed_dict={x: data})
# print(o_v)
print((o_v == target).sum())
