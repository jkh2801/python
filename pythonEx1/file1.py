'''
Created on 2020. 8. 13.

@author: GDJ24
'''
infp = None
inStr = ""
''' 파일 이름, 모드, 인코딩 방식
파일모드 : 
"r" : 읽기모드
"w" : 쓰기모드
"r+" : 읽기 쓰기 모드
"a" : append의 약자로 쓰기 모드는 되는데 기존 파일이 있는 경우에 내용이 추가된다.
"t" : Text 모드. 문자형, 생략가능, 기본형
"b" : Binary 모드, 이진형 (바이트형)
'''
infp = open("db5.py", "rt", encoding="UTF8")
while True :
    inStr = infp.readline()
    if not inStr :
        break
    print(inStr, end="")
infp.close()