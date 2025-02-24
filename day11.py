import numpy as np

v = np.array([1, 3.9, -9, 2])
print(v, v.ndim)

# np.array 는 한가지 타입으로 일괄적으로 변환해서 처리
# numpy 는 c/c++ 로 만듬
# n.dim은 배열의 차원 수를 나타내는 속성
# n.shape는 배열의 차원의 크기를 나타내는 튜플 형태의 속성을 말함
# n.dtype 배열 요소들의 데이터 타입(일괄적으로 변환해서 처리)
# n.strides 한마디로 배열 요소의 크기 (원소간의 간격, 열 간의 간격, 면간의 간격)
# float64 >> c++에서 double, go언어도 float64
