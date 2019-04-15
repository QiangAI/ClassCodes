import sklearn.datasets

data, target = sklearn.datasets.load_iris(return_X_y=True)
print(type(data), type(target))
