import pandas as pd

# Series : 1차원 자료구조로, 인덱스(index)와 값(value)으로 구성됨.
#          Python의 리스트나 NumPy 배열과 유사하지만, 인덱스를 지정할 수 있음.
#          데이터 분석에서 한 개의 열(column)처럼 활용 가능.

s = pd.Series([1, 2, 3, 4])  # 기본적으로 정수형 인덱스(0~n-1)가 자동 생성됨
s_named = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])  # 사용자 지정 인덱스
print(s_named)

# Series 슬라이싱 (1번 인덱스부터 3번 인덱스까지 선택, 4번 인덱스는 포함되지 않음)
s2 = pd.Series([99, 100, 98, 91, 92])
s2_subset = s2[1:4]
print(s2_subset)

# DataFrame : 2차원 테이블 형태의 자료구조로, 여러 개의 Series 객체가 모여 행(row)과 열(column)로 구성됨.
#             엑셀 스프레드시트나 SQL 테이블과 유사하며, 다양한 유형의 데이터를 관리하고 조작하는 데 사용됨.

df = pd.DataFrame({
    "a": [4, 5, 6],
    "b": [7, 8, 9],
    "c": [10, 11, 12]
}, index=[1, 2, 3])

print("📌 원본 DataFrame:")
print(df)

# 🔹 pd.melt() : Wide → Long 형태 변환 (데이터 변형)
df_melted = pd.melt(df).rename(columns={'variable': 'var', 'value': 'val'}).query('val > 10')
print("\n📌 Melt 적용 후 (val > 10):")
print(df_melted)

# 🔹 DataFrame 행/열 선택 방법
df_row_iloc = df.iloc[1:2]  # 숫자 인덱스 기준 (2는 포함되지 않음)
df_row_loc = df.loc[1:2]  # 라벨(이름) 기준 (1~2 포함)
df_column_subset = df.iloc[:, [0, 2]]  # 모든 행을 가져오면서, 0번째(‘a’)와 2번째(‘c’) 열을 선택

print("\n📌 iloc으로 행 선택:")
print(df_row_iloc)
print("\n📌 loc으로 행 선택:")
print(df_row_loc)
print("\n📌 iloc으로 특정 열 선택:")
print(df_column_subset)

# 🔹 apply() vs applymap()
def square(n) -> int:
    return n * n  # 각 숫자를 제곱하는 함수

print("\n📌 apply() 사용 (열 단위 연산):")
print(df.apply(lambda x: x * x))  # 열(column)별로 x*x 연산 수행

print("\n📌 applymap() 사용 (각 개별 원소 연산):")
print(df.applymap(square))  # 각 원소(element)별로 square() 함수 적용

# 🔹 DataFrame 연산 예제
print("\n📌 열(column)별 합계:")
print(df.apply(sum))  # 각 열(column)별 합계 계산

print("\n📌 행(row)별 합계:")
print(df.apply(sum, axis=1))  # 각 행(row)별 합계 계산
