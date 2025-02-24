import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression  #사이킷 런이라 부름, 선형 회귀 모델
# from sklearn.neighbors import KNeighborsRegressor  # k=최근접 이웃 회귀
from cjlearn import LinearRegression

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
# print(ls)
X = ls[['GDP per capita (USD)']].values  # 독립 변수 (입력값), 출력하면 2차원 리스트임, 입력 양식이 기본적으로 2차원 배열
y = ls[["Life satisfaction"]].values  # 종속 변수 계산 값, 출력하면 2차원 리스트임, 입력 양식이 기본적으로 2차원 배열
# values는 레이블 없이 값만 가져온다

# ls.plot(kind="scatter", grid=True, x = 'GDP per capita (USD)', y="Life satisfaction")  # grid는 바둑판이 나옴 그래프 격자 출력 여부
# plt.axis([23500, 62500, 4, 9])  #x축은 23500 에서 62500, y축은 4에서 9
# plt.show()

model = LinearRegression()  # 모델 선택 (선형 회귀 모델, gdp별 삶의 만족도 관계를 분석하기 위함)
# model = KNeighborsRegressor(n_neighbors=3)  # k-최근접 이웃 회귀

model.fit(X, y)  #모델을 훈련  X는 입력값 y 값은 정답들 레이블 위에 x, y와 fit 함수로 ax + b 에 a와 b가 머신이 알아서 정해줌

X_new = [[33121.37]]  # rok 2020 gdp for person
print(model.predict(X_new))  # 예측을 만듬 모델로 예측값 프린트

# LinearRegression 5.90
# KNeighborRegressor 5.7