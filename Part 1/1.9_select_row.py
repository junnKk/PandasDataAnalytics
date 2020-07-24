# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:38:04 2020

@author: wnsru
"""


import pandas as pd 

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data={'수학': [90, 80, 70], '영어': [98, 89, 95], '음악':[85, 95, 100], '체육':[100, 95, 90]}

df = pd.DataFrame(exam_data, index = ['재령', '준경', '현아'])
print(df)
print('\n')

# 행 인덱스를 사용하여 행 1개 선택
label1 = df.loc['재령']
position1 = df.iloc[0]
print(label1)
print('\n')
print(position1)
print('\n')

# 행 인덱스를 사용하여 2개 이상의 행 선택
label2 = df.loc[['재령','현아']]
position2 = df.iloc[[0,2]]
print(label2)
print('\n')
print(position2)
print('\n')

# 행 인덱스의 범위를 지정하여 행 선택
label3 = df.loc['재령': '준경']
position3 = df.iloc[0:2]
print(label3)
print('\n')
print(position3)