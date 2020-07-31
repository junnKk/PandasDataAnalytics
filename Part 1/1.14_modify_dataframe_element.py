# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:12:32 2020

@author: wnsru
"""


"""
원소 값 변경: DataFrame 객체의 일부분 또는 원소를 선택 = 새로운 값
"""

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['재령', '준경', '현아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 저장하고, df 객체에 변경사항 반영
df.set_index('이름', inplace=True)
print(df)
print('\n')

# 데이터프레임 df의 특정 원소를 변경하는 방법 : '재령'의 '체육'
df.iloc[0][3]=80
print(df)
print('\n')

df.loc['재령']['체육']=70
print(df)
print('\n')

df.loc['재령','체육']=90
print(df)


# df의 원소 여러 개를 변경하는 방법 : '재령'의 '음악','체육'
df.loc['재령',['음악','체육']]=50
print(df)
print('\n')

df.loc['재령',['음악','체육']]= 100, 90
print(df)