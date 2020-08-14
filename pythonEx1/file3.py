'''
Created on 2020. 8. 13.

@author: GDJ24
'''
infp, outfp = None, None
infp = open("db5.py", "rt", encoding="UTF8")
outfp = open("db5.bak","w",encoding="UTF8")
while True :
    inStr = infp.readline()
    if not inStr :
        break
    outfp.writelines(inStr)
infp.close()
outfp.close()
print("프로그램 종료")