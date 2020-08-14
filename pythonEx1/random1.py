'''
Created on 2020. 8. 6.

@author: GDJ24
'''
import random # 모듈을 로드, 모듈의 멤버를 이용한다.
rnum = random.randrange(1, 100) # 1 ~ 99의 임의의 숫자
i = 0
while True : # True: 예약어 while 구문을 무한 반복
    a = int(input("숫자를 입력하세요."))
    if a > rnum :
        print("작은 수 입니다.")
    elif a  < rnum :
        print("큰 수 입니다.")
    else :
        print("정답입니다.")
        break
    i += 1
print("%d번 만에 맞췃습니다." % i)