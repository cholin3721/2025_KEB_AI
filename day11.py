import numpy as np
import pandas as pd


df = pd.DataFrame(
 {"a" : [4, 5, 6],
        "b" : [7, 8, 9],
        "c" : [10, 11, 12]}, index=[1, 2, 3])  # key들은 컬럼 index row 열
print(df.head())
print()

df2 = pd.DataFrame(
 [[4, 7, 10],
        [5, 8, 11],
        [6, 9, 12]], index=[1, 2, 3], columns=['a', 'b', 'c'])  # key들은 컬럼 index row 열
print(df2)

print("-"* 20)

v = np.array([1, 3.9, -9, 2])


print(v, v.ndim)


# zeros(), ones() : 주어진 모양(shape)에 대해 모든 요소가 0또는 1인 배여릉ㄹ 생성하는 함수
ones = np.ones((3,4))
print(ones)

zeros = np.zeros((3,4), dtype = np.int16)  # 타입 지정도 가능하다.
print(zeros)

zeros2 = np.zeros((2,3,4))  # 타입 지정도 가능하다. 기본이 float64 인듯?
print(zeros2, zeros2.dtype)

a = np.arange(5)
print(a, a.ndim, a.shape, a.size)

a2 = np.arange(5, 11)
print(a2, a2.ndim, a2.shape, a2.size)

a3 = np.arange(5, 11, 2)
print(a3, a3.ndim, a3.shape, a3.size)

a4 = np.arange(2.0, 11.8, 0.2)
print(a4, a4.ndim, a4.shape, a4.size)

a5 = np.arange(2.0, 11.8, 2.0, dtype=np.int16)
print(a5, a5.ndim, a5.shape, a5.size)

# np.array 는 한가지 타입으로 일괄적으로 변환해서 처리
# numpy 는 c/c++ 로 만듬
# n.ndim은 배열의 차원 수를 나타내는 속성
# n.shape는 배열의 차원의 크기를 나타내는 튜플 형태의 속성을 말함
# n.dtype 배열 요소들의 데이터 타입(일괄적으로 변환해서 처리)
# n.strides 한마디로 배열 요소의 크기 (원소간의 간격, 열 간의 간격, 면 간의 간격)
# float64 >> c++에서 double, go언어도 float64
# n.size는 배열의 총 원소 개수를 반환하는 속성 요소 개수

# numpy.linspace(start, stop, num=50, endpoint=True, dtype=None)
# 지정한 범위에서 num 개의 등간격 숫자 배열을 생성
# start: 시작 값
# stop: 끝 값
# num: 생성할 숫자 개수 (기본값: 50)
# endpoint=True: stop 포함 여부 (False로 설정하면 stop 제외)

# numpy.reshape(arr, newshape)
# 배열의 형태(차원)를 변경
# 기존 원소 개수(size)는 그대로 유지해야 함
# newshape에 -1을 사용하면 자동 계산