# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:25:47 2020

@author: wnsru
"""

"""
행 인덱스 변경: DataFrame 객체.rename(index={기존 인덱스:새 인덱스,...})
열 이름 변경 : DataFrame 객체.rename(colunms ={기존 이름 : 새 이름 ,...})
"""

import pandas as pd

# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '지산중'], [15,'여','해솔중']],index=['상우','진희'],columns=['나이','성별','학교'])

# 데이터프레임 출력
print(df) 
print('\n')

# 열 이름 중 '나이'를 '연령'으로, '학교'를 '소속'으로 바꾸기
df.rename(columns={'나이':'연령', '학교':'소속'}, inplace=True)

# 행 인덱스 중에서 '상우'를 '학생1'로, '진희'를 '학생2'로 바꾸기
df.rename(index={'상우':'학생1','진희':'학생2'}, inplace=True)

# df 출력(변경 후)
print(df)
