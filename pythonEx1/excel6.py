'''
Created on 2020. 8. 18.

@author: GDJ24
'''
import pandas as pd
infile = "sales_2015.xlsx"
outfile = "sales_2015_pd.xlsx"
# read_excel(file 이름, sheet 이름, 인덱스 여부)
df = pd.read_excel(infile, "january_2015", index_col=None)
print(df)
# df 조건 : Sale Amount 값이 500보다 큰 값만 outfile에 젖아하기
df_value = df[df["Sale Amount"].astype(float) > 500.0]
# ExcelWriter(출력파일 이름, xls 기본)
# engine = "openpyxl" : xlsx 파일로 출력
writer = pd.ExcelWriter(outfile,engine="openpyxl")
# to_excel : DataFrame 데이터를 excel 파일로 변환
df_value.to_excel(writer,sheet_name="jan_15_out",index=False)
writer.save()