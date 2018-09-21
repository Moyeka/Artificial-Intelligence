#K近邻算法

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets

#引入数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

#将原始数据划分为训练、测试数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.preprocessing import StandardScaler
#数据归一化
standardscaler = StandardScaler()
standardscaler.fit(X_train)

X_train = standardscaler.transform(X_train)
X_test = standardscaler.transform(X_test)


from sklearn.neighbors import KNeighborsClassifier
#KNN算法
knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(X_train, y_train)

y_predict = knn_clf.predict(X_test)
print(y_test)
print(y_predict)

sco = knn_clf.score(X_test, y_test)
print(sco)

#网格搜索
param_grid = [
    {
        'weights':['uniform'],
        'n_neighbors':[i for i in range(1,11)]
    },
    {
        'weights' :['distance'],
        'n_neighbors':[i for i in range(1,11)],
        'p':[i for i in range(1, 6)]
    }
]

from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(knn_clf, param_grid)

grid_search.fit(X_train, y_train)
knn_clf = (grid_search.best_estimator_)

print(knn_clf)
print(grid_search.best_score_)









