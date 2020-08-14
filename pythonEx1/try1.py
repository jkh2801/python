'''
Created on 2020. 8. 10.

@author: GDJ24
예외 처리
'''
mystr = "파이썬 공부 중입니다. 열심히 파이썬을 공부합시다."
strpos = [] # 파이썬 문자의 위치 정보 저장
index = 0
while True :
    try :
        index = mystr.index("파이썬",index) 
        strpos.append(index)
        index += 1
    except :
        break
    
print("파이썬 문자의 위치: ",strpos,", 문자 갯수: ",len(strpos))

ss = "홍길동"
# 홍#길#동# 로 출력하기
for i in range(0, len(ss)) :
    print(ss[i],end="#")
print()
## 동길홍 으로 출력하기
print(ss[::-1])
