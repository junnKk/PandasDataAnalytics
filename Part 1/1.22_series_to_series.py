# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:31:03 2020

@author: wnsru
"""


"""
시리즈와 시리즈 연산 : Series1 + 연산자(+, - , *, /) + Series2
"""

import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기 
student1 = pd.Series({'국어':100, '영어' : 80, '수학' : 90})
student2 = pd.Series({'수학':80, '국어' : 90, '영어' : 80})
print(student1)
print('\n')
print(student2)
print('\n')

# 두 학생의 과목별 점수로 사칙연산 수행
addition = student1 + student2
substraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))
print('\n')

# 사칙연사 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
result = pd.DataFrame([addition, substraction, multiplication, division], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)