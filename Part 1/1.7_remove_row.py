# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:25:48 2020

@author: wnsru
"""


import pandas as pd 

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data={'수학': [90, 80, 70], '영어': [98, 89, 95], '음악':[85, 95, 100], '체육':[100, 95, 90]}

df = pd.DataFrame(exam_data, index = ['재령', '준경', '현아'])
print(df)
print('\n')

# 데이터프레임 df를 복제하여 변수 df2에 저장. df2의 1개 헹(row) 삭제
df2 = df[:]
df2.drop('준경',inplace=True)
print(df2)
print('\n')

# 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 헹(row) 삭제
df3 = df[:]
df3.drop(['준경', '현아'],axis=0,inplace=True)
print(df3)