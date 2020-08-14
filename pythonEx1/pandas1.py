'''
Created on 2020. 8. 14.

@author: GDJ24
'''
import pandas as pd # pip install pandas
df = pd.DataFrame({"A":[1,4,7],"B":[2,5,8],"C":[3,6,9]})
print(type(df))
print(df)

print("인덱스 값 조회하기")
print(df.iloc[0])
print(df.iloc[1])
print(df.loc[1])
#print(df.ix[0]) # 버전2와 버전 3 초기에 사용됬던 명령어

#열 선택
print(df["A"])

df = pd.DataFrame(data=([[1,2,3],[4,5,6],[7,8,9]]), index=[2,"A",4],columns=[51,52,54])
print(df)
print(df.iloc[2])
print(df[51])