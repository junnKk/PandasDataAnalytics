# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:46:46 2020

@author: wnsru
"""

"""
열 추가
데이터프레임 객체['추가하려는 열 이름'] = 데이터 값
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

# df에 '국어' 열 추가. 데이터 값은 80으로 지정
df['국어']=80
print(df)