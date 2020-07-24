# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:16:10 2020

@author: wnsru
"""


import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['재령', '준경', '현아'],
             '수학' : [90, 80, 100],
             '영어' : [100, 90, 90],
             '음악' : [100, 100, 100],
             '체육' : [90, 100, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

# '수학' 점수 데이터만 선택. 변수 math1에 저장 -> 열 1개 선택 시, 시리즈 반환
math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

# '영어' 점수 데이터만 선택. 변수 english에 저장 -> 열 1개 선택 시, 시리즈 반환
english = df.영어
print(english)
print(type(english))

# '음악', '체육' 점수 데이터를 선택. 변수 music_gym에 저장 -> 이중대괄호([[]]) 사용 시, 데이터프레임 반환
music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

# '수학' 점수 데이터만 선택. 변수 math2에 저장 -> 이중대괄호([[]]) 사용 시, 데이터프레임 반환
math2 = df[['수학']]
print(math2)
print(type(math2))