'''
Created on 2020. 8. 5.

@author: GDJ24

python2.py : input(), print() 함수
input("입력전 출력 문자열") : 입력받은 값은 문자열 형태로 입력받는다.
print(출력값1, 출력값2, ...) : 여러개를 출력시 반점(,)으로 연결이 가능하다.

'''
a = int(input("값1 입력: "))
b = int(input("값2 입력: "))
result = a+b;
print(a,"+",b,"=",result)
print("%d + %d = %d" % (a,b,result))
print("{0:d} + {1:d} = {2:d}".format(a,b,result))
print("안녕하세요",end="")
print("홍길동입니다.")
print("동해물과 백두산이 "+"마르고 닳도록")
print("""동해물과 백두산이 
마르고 닳도록""")