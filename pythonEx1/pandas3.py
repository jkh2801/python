'''
Created on 2020. 8. 14.

@author: GDJ24
'''
import pandas as pd

infile = "supplier_data.csv"
outfile = "pandasSupplier.csv"
df = pd.read_csv(infile)
print(df)

'''
    부분 DataFrame 객체 생성 : Purchase Date 열의 값 중 importDate 속한 모든 컬럼을 조회
'''
importDate = ["1/20/14", "1/30/14"]
df_inset = df.loc[df["Purchase Date"].isin(importDate),:]
print(df_inset)
print(type(df_inset))