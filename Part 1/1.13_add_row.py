# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:54:51 2020

@author: wnsru
"""


import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['재령', '준경', '현아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 새로운 행(row)에 추가 - 같은 원소 값 입력
df.loc[3]= 0
print(df)
print('\n')

# 새로운 행(row) 추가 - 원소 값 여러 개의 배열 입력 
df.loc[4]= ['진희 ', 90,80,70,60]
print(df)
print('\n')

# 새로운 행(row) 추가 - 기존 행 복사
df.loc['행5'] = df.loc[3]
print(df)
