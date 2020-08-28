'''
Created on 2020. 8. 18.

@author: GDJ24
'''
from xlrd import open_workbook
from xlwt import Workbook #pip install xlwt
infile = "ssec1804.xls"
outfile = "ssec1804out.xls" # 출력일 xls 팡리 선택

outworkbook = Workbook() # 비어있는 xls 파일
out_sheet = outworkbook.add_sheet("전체증감") # sheet 추가

# workbook : infile의 내용을 저장 (xls 파일 전체)
with open_workbook(infile) as workbook :
    worksheet = workbook.sheet_by_name("1.전체증감") # worksheet : sheet 이름이 "1.전체증감" 인 데이터 저장
    for rindex in range(worksheet.nrows) :
        for cindex in range(worksheet.ncols) :
            out_sheet.write(rindex, cindex, worksheet.cell_value(rindex, cindex))
            print(worksheet.cell_value(rindex, cindex))
outworkbook.save(outfile)  # xls 파일을 file로 저장