import cv2
import sklearn.datasets
import tushare as tu

# http://tushare.waditu.com/index.html#id5
# pandas.core.frame.DataFrame:数据分析
result = tu.get_industry_classified()
print(type(result))
print(result)

# numpy.ndarray  ； 机器学习
data, target = sklearn.datasets.load_iris(return_X_y=True)
print(type(data))

# 图像numpy.ndarray
img = cv2.imread('baidu.png')
print(type(img))

# 数据可视化：matplotlib：ndarray + DataFrame
