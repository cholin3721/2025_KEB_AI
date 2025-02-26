import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


mpg = sns.load_dataset('mpg')


# "origin" 컬럼 원-핫 인코딩
mpg_encoder = OneHotEncoder(sparse_output=False)  # sparse=False로 설정하여 바로 배열 반환
mpg_origin_1hot = mpg_encoder.fit_transform(mpg[['origin']])

mpg_origin_1hot_df = pd.DataFrame(mpg_origin_1hot, columns=mpg_encoder.get_feature_names_out(['origin']))

mpg.drop("origin", axis=1, inplace=True)
mpg = pd.concat([mpg, mpg_origin_1hot_df], axis=1)

X = mpg.drop(columns=['name','mpg'])
y = mpg['mpg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sc = StandardScaler(with_mean=False)

X_train = sc.fit_transform(X_train)



