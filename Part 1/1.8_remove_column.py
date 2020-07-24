# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:29:10 2020

@author: wnsru
"""


import pandas as pd 

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data={'수학': [90, 80, 70], '영어': [98, 89, 95], '음악':[85, 95, 100], '체육':[100, 95, 90]}

df = pd.DataFrame(exam_data, index = ['재령', '준경', '현아'])
print(df)
print('\n')

# 데이터프레임 df를 복제하여 변수 df4에 저장. df4의 한 개의 열 삭제
df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')

# 데이터프레임 df를 복제하여 변수 df5에 저장. df5의 2 개의 열 삭제
df5 = df[:]
df5.drop(['영어','체육'],axis=1, inplace=True)
print(df5)