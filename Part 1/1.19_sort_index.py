# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:46:38 2020

@author: wnsru
"""


"""
행 인덱스 기준 정렬 : DataFrame 객체.sort_index()
- > 오름차순 : ascending = True 
- > 내림차순 : ascendnig = False
"""

import pandas as pd 

# 딕셔너리 정의 
dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

# 딕셔너리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r3]로 지정
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
print('\n')

# 내림 차순으로 행 인덱스 정렬 
ndf = df.sort_index(ascending = False)
print(ndf)
