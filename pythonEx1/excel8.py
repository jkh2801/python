'''
Created on 2020. 8. 19.

@author: GDJ24
sales_2015.xlsx 파일 중 
sheet = january_2015 인 sheet에서
Customer Name 컬럼의 값이 J으로 시작하는 행만 선택하여 Sales_2015_3.xlsx 파일로 생성하기
'''
import pandas as pd
infile = "sales_2015.xlsx"
outfile = "sales_2015_3.xlsx"
df = pd.read_excel(infile, "january_2015", index_col=None)
df_value = df[df["Customer Name"].str.startswith("J")]
writer = pd.ExcelWriter(outfile,engine="openpyxl")
df_value.to_excel(writer, sheet_name="sale_2015", index=False)
writer.save()