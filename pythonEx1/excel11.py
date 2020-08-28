'''
Created on 2020. 8. 19.

@author: GDJ24
pandas를 이용하여 xls 파일 읽기
-- 출력되는 excel 파일의 sheet를 여러개로 저장하기
'''
import pandas as pd
infile = "ssec1804.xls"
outfile = 'ssec1804_bok.xls'
writer = pd.ExcelWriter(outfile) # 출력팡리 설정
df = pd.read_excel(infile, sheet_name=None, index_col=None)
for worksheet_name, data in df.items() :
    print("===",worksheet_name,"===")
    print(data)
    data.to_excel(writer, sheet_name=worksheet_name, index=False, header=False)
writer.save()