'''
Created on 2020. 8. 19.

@author: GDJ24
= pandas를 이용하여 xlsx 파일 읽기
1. xlsx 파일의 모든 sheet 데이터 읽기
2. 생성되는 excel 파일로 하나의 sheet로 데이터 저장 ==> 조건이 맞는 경우만
'''
import pandas as pd
infile = "sales_2015.xlsx"
outfile = "sales_all.xlsx"
df = pd.read_excel(infile, sheet_name=None, index_col=None)
row_output = [] # 모든 sheet의 데이터 저장
# df.items() : sheet 정보들 (sheet 이름, sheet 데이터)
for worksheet_name, data in df.items() :
    print("===",worksheet_name,"===")
    row_output.append(data[data["Sale Amount"].replace("$","").replace(",","").astype(float) > 200.0])
filtered_row = pd.concat(row_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(outfile,engine="openpyxl")
filtered_row.to_excel(writer, sheet_name="sale_2015", index=False)
writer.save()