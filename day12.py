import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import accuracy_score

# df = pd.DataFrame({
#     'A' : [1, 2, np.nan, 4],
#     'B' : [np.nan, 2, 3, 4],
#     'c' : [1, 2, 3, 4]
# })
#
# print(df)
# print()

# 사이킷런을 사용하지 않고 산술평균으로 채워넣는 방법

# mean = df.mean().round(2)
# df.fillna(mean, inplace= True)
# print(df)

# i = SimpleImputer(strategy="mean")
# df = df.select_dtypes(include=[np.number])
# df = pd.DataFrame(i.fit_transform(df))
# print(df)

# df = df.replace(np.nan, df.mean())
# print(df)

titanic = sns.load_dataset('titanic')

print(titanic.info())
titanic.dropna(subset = ["age"], inplace = True)

X = titanic[['age']]
y = titanic[['survived']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

model = KNeighborsRegressor(n_neighbors = 5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(5,2))
plt.scatter(X_test, y_test, color = 'blue', label = 'Real')
plt.scatter(X_test, y_pred, color = 'red', label = 'Predicted')
plt.title('KNeighborsRegressor: Real vs Predicted')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.show()

