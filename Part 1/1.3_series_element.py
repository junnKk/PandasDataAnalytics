import pandas as pd

# tuple을 시리즈로 변환(인덱스 옵션 지정)
tup_data = ('준경', '1998-03-24', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)
print('\n')

# 원소를 1개 선택
print(sr[0])
print(sr['이름'])
print('\n')

# 여러 개의 원소를 선택(인덱스 리스트 활용)
print(sr[[1,2]])
print(sr[['생년월일','성별']])
print('\n')

# 여러 개의 원소를 선택(인덱스 범위 지정)
print(sr[1:4])
print(sr['생년월일':"학생여부"])