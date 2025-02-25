import numpy as np
import pandas as pd

class LinearRegression:
    def __init__(self):
        self.slope = None  # weight
        self.intercept = None  # bias

    def fit(self, X, y):
        """
        learning fuction
        :param x: independent variable(2d array format)
        :param y: dependent variable (2d array format)
        :return:
        """
        X_mean = np.mean(X)
        y_mean = np.mean(y)

        denominator = np.sum(pow(X-X_mean, 2))
        numerator = np.sum((X - X_mean) * (y - y_mean))  # numpy

        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * X_mean)


    def predict(self, X) -> np.ndarray:
        """
        predict value for input
        :param X: new independent variable
        :return: predict value for input (2d array format)
        """
        return self.slope * np.array(X) + self.intercept

class KNeighborsRegressor :
    def __init__(self, n_neighbors = 5):
        self.n_neighbors = n_neighbors
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = X
        self.y = y


    def predict(self, num):
        a = [(abs(num[0][0] - j[0]), i) for i, j in enumerate(self.X)]
        sorted_neighbor = sorted(a, key=lambda x : x[0])[:self.n_neighbors]
        total = 0
        for _, i in sorted_neighbor :
            total +=self.y[i]
        return total / self.n_neighbors

# 교수님 코드
# class KNeighborsRegressor:
#     def __init__(self, n_neighbors=5):  # default neighbor
#         self.n_neighbors = n_neighbors
#
#
#     def fit(self, X_train, y_train):
#         """
#         learning function
#         :param X: independent variable (2d array format)
#         :param y: dependent variable (2d array format)
#         :return: void
#         """
#         self.X_train = X_train
#         self.y_train = y_train
#
#
#     def predict(self, X_test):
#         """
#         predict value for input
#         :param X: new indepent variable
#         :return: predict value for input (2d array format)
#         """
#         predictions = []
#         for x_test in X_test:  # loop just one time in this example
#             # d(P, Q) = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#             distances = np.sqrt(np.sum((x_test - self.X_train)**2, axis=1))
#             # print(distances)
#             indices = np.argsort(distances)[:self.n_neighbors]  # 정렬
#             # print(indices)  # index의 복수형
#             prediction = np.mean(self.y_train[indices])
#             # prediction = (self.y_train[indices[0]]+self.y_train[indices[1]]+self.y_train[indices[2]]) / self.n_neighbors
#             predictions.append(prediction)
#
#             return np.array(prediction).reshape(-1, 1)


