import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pystan==2.19.1.1 이 설치되어 있어야 prophet 을 설치할 수 있다
'''
페이스북에서 개발한 Time Series (시계열) 데이터 모델링 라이브러리를 가지고 놀아보자
'''
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.options.display.max_rows

df = pd.read_csv('./data_toy/avocado-updated-2020.csv') # 15 ~ 20년도 아보카도 시세 데이터셋, 데이터 프레임에 담기

print(df.shape)
# print(f'헤드 데이터\n {df.head()}')
print(''.join(['_' for i in range(100)]))
# print(df.describe()) # 개요
# print(df.groupby('type').mean())

df = df.loc[(df.type == 'conventional') & (df.geography == 'Total U.S.')] # 데이터 전처리 (미국, 일반 아보카도)

# print(df.head())

df['date'] = pd.to_datetime(df['date'])

data = df[['date', 'average_price']].reset_index(drop=True) # 데이터 전처리 (날짜, 평균가격만 포함, index값 초기화)
data = data.rename(columns={'date' : 'ds', 'average_price' : 'y'})


# print (data.head())

# plt.plot(x=data['ds'], y=data['y'])
# print(data['ds'])
# print(data['y'])
model =
data.plot(x='ds', y='y', figsize=(14, 7))

# plt.figure()
plt.show()