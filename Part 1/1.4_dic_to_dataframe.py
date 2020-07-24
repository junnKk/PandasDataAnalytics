# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:21:38 2020

@author: wnsru
"""

"""
딕셔너리-> 데이터프레임 변환 : pandas.DataFrame(딕셔너리 객체)
"""


import pandas as pd 

# 열 이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dic_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12]}

# 판다스 DataFrame() 함수로 딕셔너리 데이터프레임으로 변환. 변수 df에 저장
df = pd.DataFrame(dic_data)

# df의 자료형 출력
print(type(df))
print('\n')

# 변수 df에 저장되어있는 데이터프레임 객체를 출력
print(df)
