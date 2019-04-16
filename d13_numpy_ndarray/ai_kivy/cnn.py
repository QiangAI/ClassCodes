# coding= utf-8
import tensorflow as tf

# -----------------
# 下面是按照Lenet-5模型构建，该神经网络模型是因为手写数字识别而闻名；
# 而且该模型在人脸识别也有不错的效果；
# -----------------
# 定义神经网络模型=================
# 定义输入
x = tf.placeholder(tf.float32, [None, 32, 32, 3])
y = tf.placeholder(tf.float32, [None, 4])


# 定义训练系数
# 定义系数模板
def get_weights(shape):
    w_init = tf.random.truncated_normal(shape=shape, mean=0, stddev=0.1, dtype=tf.float32)  # 给被训练的变量一个初始值
    b_init = tf.random.truncated_normal(shape=[shape[-1]], mean=0, stddev=0.1, dtype=tf.float32)

    w = tf.Variable(initial_value=w_init)
    b = tf.Variable(initial_value=b_init)
    return w, b


# 定义运算
def layer(in_x, in_w, in_b, padding='VALID'):
    o = tf.nn.conv2d(input=in_x, filter=in_w, strides=[1, 1, 1, 1], padding=padding)
    o = tf.math.add(o, in_b)
    o = tf.nn.relu(o)
    o = tf.nn.avg_pool(value=o, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    return o


# 卷积1
w1, b1 = get_weights(shape=[5, 5, 3, 6])
o1 = tf.nn.conv2d(input=x, filter=w1, strides=[1, 1, 1, 1], padding='VALID')
o1 = tf.nn.bias_add(o1, b1)
o1 = tf.nn.relu(o1)
o1 = tf.nn.avg_pool(value=o1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
o1 = tf.nn.dropout(o1, 0.80)

# 卷积2
w2, b2 = get_weights(shape=[5, 5, 6, 16])  # 这里的深度6就是上面输出的6
o2 = tf.nn.conv2d(input=o1, filter=w2, strides=[1, 1, 1, 1], padding='VALID')
o2 = tf.nn.bias_add(o2, b2)
o2 = tf.nn.relu(o2)
o2 = tf.nn.avg_pool(value=o2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
o2 = tf.nn.dropout(o2, 0.70)

# 卷积3
w3, b3 = get_weights(shape=[5, 5, 16, 120])  # 这里的深度6就是上面输出的6
o3 = tf.nn.conv2d(input=o2, filter=w3, strides=[1, 1, 1, 1], padding='VALID')
o3 = tf.nn.bias_add(o3, b3)
o3 = tf.nn.relu(o3)
o3 = tf.nn.dropout(o3, 0.50)

# 格式化，进入全连接层
o3 = tf.reshape(o3, [-1, 120])
w4, b4 = get_weights(shape=[120, 84])  # 这里的深度6就是上面输出的6
o4 = tf.nn.relu(tf.matmul(o3, w4) + b4)
o4 = tf.nn.dropout(o4, 0.50)

w5, b5 = get_weights(shape=[84, 4])  # 这里的深度6就是上面输出的6
o5 = tf.nn.softmax(tf.matmul(o4, w5) + b5)

y_ = o5
# 定义损失函数
loss = tf.losses.sigmoid_cross_entropy(y, y_)
# loss = tf.losses.mean_squared_error(y, y_)
# 定义训练算法
# optimizer = tf.train.GradientDescentOptimizer(0.0001)
optimizer = tf.train.AdamOptimizer(0.0001)
trainer = optimizer.minimize(loss)
