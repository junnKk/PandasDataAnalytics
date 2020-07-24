# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:29:21 2020

@author: wnsru
"""


import pandas as pd

# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '지산중'], [15,'여','해솔중']],index=['상우','진희'],columns=['나이','성별','학교'])

# 행 인덱스, 열 이름 확인하기
print(df) # 데이터프레임
print('\n')
print(df.index) # 행 인덱스
print('\n')
print(df.columns) # 열 이름
 
# 행 인덱스, 열 이름 변경하기
df.index = ['학생1','학생2']
df.columns = ['연령','남여','소속']

print('\n')
print(df) #데이터프레임
print('\n')
print(df.index) # 행 인덱
print('\n')
print(df.columns) # 열 이름
 