'''
Created on 2020. 8. 14.

@author: GDJ24
iloc : 인덱스를 기준으로 조회
loc : 이름 기준으로 조회
'''
import pandas as pd

infile = "supplier_data.csv"
df = pd.read_csv(infile)
df_col = df.iloc[:,[0,3]] # 행[전체], 열[0과 3번열]
print(df_col)
df_col = df.iloc[0:4,0:3]
print(df_col)
df_col = df.loc[:,["Invoice Number", "Cost"]]
print(df_col)
df_col = df.loc[df["Invoice Number"].str.startswith("920-"),["Invoice Number", "Cost"]]
print(df_col)
