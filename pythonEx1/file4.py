'''
Created on 2020. 8. 13.

@author: GDJ24
'''
import os.path
file="file1.py"
if os.path.isfile(file) :
    print(file,"은 파일입니다.")
elif os.path.isdir(file) :
    print(file,"은 폴더입니다.")
if os.path.exists(file) :
    print(file,"은 존재합니다.")
else :
    print(file,"은 없는 파일입니다.")