# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:03:00 2020

@author: wnsru
"""


"""
시리즈와 숫자 연산 : Series객체 + 연산자(+, -, *, /) + 숫자
"""

import pandas as pd 

# 딕셔너리 데이터로 판다스 시리즈 만들기 
student1 = pd.Series({'국어':100, '영어' : 80, '수학' : 90})
print(student1)
print('\n')

# 학생의 과목별 성적을 200으로 나누기
percentage = student1/200

print(percentage)
print('\n')
print(type(percentage))