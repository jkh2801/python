'''
Created on 2020. 8. 19.

@author: GDJ24
'''
import pandas as pd
import glob # 경로명 표현 시 사용되는 모듈
import os # 시스템 관련 모듈
inpath = "C:/Users/GDJ24/git/python/"
outfile = "sales_all1.xlsx"
excels = glob.glob(os.path.join(inpath,"*.xlsx")) # inpath 폴더의 모든 xlsx 파일 선택
rows = [] # DataFrame 객체를 리스트로 저장하는 객체
for excel in excels :
    print(excel)
    dfs = pd.read_excel(excel, sheet_name=None, index_col=None)
    for sheet_name, df in dfs.items() :
        rows.append(df)
# excel 파일로 저장
# axis = 0 : row 추가
# df_concat : 지정된 폴더에 잇는 엑셀파일의 모든 
df_concat = pd.concat(rows, sort=False, axis = 0, ignore_index=True)
writer = pd.ExcelWriter(outfile)
df_concat.to_excel(writer, sheet_name="all_data_all_worksheet", index=False)
writer.save()