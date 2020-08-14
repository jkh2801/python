'''
Created on 2020. 8. 13.

@author: GDJ24
'''
outfp = None
outfp = open("data.txt","w",encoding="UTF8")
while True :
    outstr = input("내용 입력: ")
    if outstr != "" :
        outfp.writelines(outstr + "\n")
    else :
        break
outfp.close()
print("프로그램 종료")