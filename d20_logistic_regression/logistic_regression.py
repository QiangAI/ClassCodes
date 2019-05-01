import numpy as np
import sklearn.datasets as ds


class GradientOptimizer:
    def __init__(self, eta_):  # eta控制下降速度：学习率learning_rate
        self.eta = eta_
        # S函数
        self.sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))  # forward计算输出需要
        # S函数的导数
        self.sigmoid_d = lambda x: self.sigmoid(x) * (1 - self.sigmoid(x))  # backward计算增量需要
        # 损失函数
        self.cross_entropy = lambda y1, y2: y1 * np.log(y2) + (1 - y1) * np.log(1 - y2)
        # 损失函数的导数
        self.cross_entropy_d = lambda y1, y2: (y1 - y2) / (y2 * (1 - y2))

        # 初始化一个权重系数矩阵（把权重系数分成：权重 + bias截距项）
        self.W = np.random.uniform(low=-0.1, high=0.1, size=(4, 1))
        self.b = np.random.uniform(low=-0.1, high=0.1, size=(1, 1))  # 截距b xW + b

    def forward(self, data_):
        self.data = data_
        # 2. 计算输出-线性输出xW(W随机取得权重)
        print('\t\t\t计算线性值')
        self.y_linear = np.matmul(self.data, self.W) + self.b
        # 3. 使用逻辑分布输出概率S(xW)：计算误差
        print('\t\t\t使用S函数计算概率输出')
        self.y_sigmoid = self.sigmoid(self.y_linear)
        # return self.y_sigmoid
        # print(self.y_sigmoid)

    def backward(self, target_):
        # 4. 计算梯度
        print('\t\t\t计算梯度')
        self.target = target_
        # 损失函数的导数(比起我们原来的公式缩小了样本总数倍)
        v1 = self.cross_entropy_d(self.target, self.y_sigmoid)  # * len(self.data)
        # S函数的导数
        v2 = self.sigmoid_d(self.y_linear)
        # 计算增量
        v = v1 * v2

        self.w_delta = - (v * self.data).mean(axis=0)
        self.b_delta = - v.mean(axis=0)

        self.w_grad = self.eta * self.w_delta
        self.b_grad = self.eta * self.b_delta

        self.w_delta = self.w_delta.reshape(self.W.shape)
        self.b_delta = self.b_delta.reshape(self.b.shape)

        # 5. 更新权重矩阵W
        print('\t\t\t更新权重')
        self.W -= self.w_delta
        self.b -= self.b_delta
        print(self.W)

    def update(self, data_, target_):
        print('\t\t\t向前计算输出值')
        self.forward(data_)
        print('\t\t\t向后更新权重W')
        self.backward(target_)

    def predict(self, data_):
        # return self.forward(data_)
        self.forward(data_)
        return self.y_sigmoid


class Trainer:

    def __init__(self, data_, target_, num_, eta_):
        self.data = data_
        self.target = target_

        self.train_num = num_  # 训练次数
        self.eta = eta_

        self.opt = GradientOptimizer(self.eta)

    def train(self):
        # 6. 训练：反复执行N遍（使用训练样本开始计算）
        # 循环调用opt来反复更新权重
        for n in range(self.train_num):
            print(F'\t\t第{n}轮训练----------------------')
            self.opt.update(self.data, self.target)  # 训练，传递训练数据

    def evaluate(self):
        # 7. 测试评估（准确率）
        # 对所有已知训练样本进行预测
        result = self.opt.predict(self.data)
        a_cls = result[0:50]  # A类的预测
        b_cls = result[50:100]  # B类的预测
        print(a_cls)
        print('------')
        print(b_cls)

        a_num = (a_cls < 0.01).sum()
        b_num = (b_cls > 0.99).sum()
        print(F'A类的数量：{a_num}')
        print(F'B类的数量：{b_num}')


class LogisticRegressionApp:

    # 1. 数据准备
    def __init__(self):
        # 加载数据
        self.data, self.target = ds.load_iris(return_X_y=True)
        self.data = self.data[0:100]
        self.target = self.target[0:100]
        self.target = self.target.reshape((len(self.target), 1))  # 数据格式化成矩阵

        self.trainer = Trainer(self.data, self.target, 1000, 0.01)

    def run(self):
        # 训练
        print('\t开始训练')
        self.trainer.train()
        # 开始评估
        print('\t开始评估')
        self.trainer.evaluate()


app = LogisticRegressionApp()
print('开始应用')
app.run()

# 1. 在鸢尾花完成分类
#  0:100
#  50:150
#  0:50  + 100:50

# 2. 文档中：1：10000-100000  0：0-30000

# 项目：爬取首页，农产品分类，放入redis
