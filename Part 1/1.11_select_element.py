# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:12:01 2020

@author: wnsru
"""

"""
인덱스 이름 : DataFrame 객체.loc[행 인덱스, 열 이름]
정수 위치 인덱스 : DataFrame 객체.iloc[행 번호, 열 번호]
"""


import pandas as pd 

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['재령', '준경', '현아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경 사항 저장(set_index('', inplace=True))
df.set_index('이름', inplace=True)
print(df)
print('\n')

# 데이터프레임 df의 특정 원소 1개 선택('재령'의 '음악') -> 원소 반환
a = df.loc['재령','음악']
print(a)
a = df.iloc[0,2]
print(a)
print(type(a))
print('\n')

# 데이터프레임 df의 특정 원소 2개 이상 선택 -> 시리즈 반환
b = df.loc['재령', ['음악','수학']]
print(b)
b = df.loc['재령', '수학' : '체육' :2] 
print(b)
b = df.iloc[0,[1,3]]
print(b)
b = df.iloc[0, 0::2]
print(b)
print(type(b))
print('\n')

# 데이터프레임 df 2개 이상의 행과 열에 속하는 원소들 선택 -> 데이터프레임 반환
c = df.loc[['재령', '현아'], ['수학', '체육']]
print(c)
c = df.loc[:'현아', '수학': :3]
print(c)
c = df.iloc[[0,2],[0,3]]
print(c)
c = df.iloc[0:3:2, ::3]
print(c)
print(type(c))

