# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:24:24 2020

@author: wnsru
"""

"""
새로운 배열로 행 인덱스 재지정 : DataFrame 객체.reindex( 새로운 인덱스 배열 )

fill_value
"""


import pandas as pd 

# 딕셔너리 정의 
dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

# 딕셔너리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r3]로 지정
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
print('\n')

# 인덱스를 r0~r4로 재지정
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index) # 새로운 데이터프레임 객체 반환
print(ndf)
print('\n')

# reindex로 발생한 NaN 값을 숫자 0으로 채우기
ndf2 = df.reindex(new_index, fill_value = 0)
print(ndf2)