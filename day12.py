import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame({
    'A' : [1, 2, np.nan, 4],
    'B' : [np.nan, 2, 3, 4],
    'c' : [1, 2, 3, 4]
})

print(df)
print()

# 사이킷런을 사용하지 않고 산술평균으로 채워넣는 방법

# mean = df.mean().round(2)
# df.fillna(mean, inplace= True)
# print(df)

# i = SimpleImputer(strategy="mean")
# df = df.select_dtypes(include=[np.number])
# df = pd.DataFrame(i.fit_transform(df))
# print(df)


