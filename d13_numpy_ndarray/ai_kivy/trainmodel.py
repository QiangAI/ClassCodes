# coding=utf-8
import os

import numpy as np
import tensorflow as tf
from cnn import *
from facepreprocess import FacePreprocess
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# 输入数据加载，格式化与规范处理
pp = FacePreprocess('images/', 'trains/')
print('预处理数据......')
pp.preprocess()
print('预处理数据完毕！')
print('数据加载......')
data, target, target_dict = pp.read_image()
print("样本个数：(%d)" % len(target))
labels = np.zeros((len(target), len(target_dict.items())), dtype=np.int)
for i in range(len(target)):
    lb = target[i]
    labels[i][lb] = 1
print("数据加载完毕！")
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, random_state=1)
# print(y_test)
# 训练
print("训练......")
# 定义评估模型
correct = tf.equal(tf.argmax(y_, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

# 初始化
# 模型保存文件
model_path = 'models/'
model_file = 'face.model'
if not os.path.exists(model_path):
    os.makedirs(model_path)
# 模型保存工具
saver = tf.train.Saver()
# 训练环境
session = tf.Session()
global_v = tf.global_variables()
op_init = tf.initializers.variables(global_v)
session.run(op_init)

TIMES = 1000
batch_size = 20
batch = len(X_train) // batch_size
for t in range(TIMES):
    loss_result = 0.0
    for idx in range(batch):
        _, loss_result = session.run([trainer, loss],
                                     feed_dict={
                                         x: X_train[idx * batch_size:(idx + 1) * batch_size],
                                         y: y_train[idx * batch_size:(idx + 1) * batch_size]})
    # 没一轮训练就评估效果
    if t % 5 == 0:
        correct_rate = session.run(accuracy, feed_dict={x: X_test, y: y_test})
        print('正确率: %5.2f%%，损失度：%f' % (correct_rate * 100.0, loss_result))
print('训练完毕')
print('保存模型......')
saver.save(session, os.path.join(model_path, model_file))
print('保存模型完毕')
# 训练效果分析
predict_ = tf.argmax(y_, 1)
predict_train = session.run(predict_, feed_dict={x: X_train})
predict_test = session.run(predict_, feed_dict={x: X_test})
train_y = np.argmax(y_train, 1)
test_y = np.argmax(y_test, 1)
# print('训练集:\n', predict_train)
# print('测试集:\n', predict_test)
print('训练混淆矩阵:\n', confusion_matrix(train_y, predict_train))
print('训练混淆矩阵:\n', confusion_matrix(test_y, predict_test))
print('训练集分类报告:\n', classification_report(train_y, predict_train))
print('测试集分类报告:\n', classification_report(test_y, predict_test))
