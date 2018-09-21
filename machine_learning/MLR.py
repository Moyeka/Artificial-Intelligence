#多元线性回归

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

boston = datasets.load_boston()

X = boston.data
y = boston.target
X = X[y < 50.0]
y = y[y < 50.0]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

sco1 = lin_reg.score(X_test, y_test)
print(sco1)

#KNN解决回归问题

from sklearn.neighbors import KNeighborsRegressor

knn_reg = KNeighborsRegressor()
knn_reg.fit(X_train, y_train)
sco2 = knn_reg.score(X_test, y_test)

print(sco2)









