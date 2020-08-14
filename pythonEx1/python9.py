'''
Created on 2020. 8. 6.

@author: GDJ24
삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램을 작성
'''
print("삼강형의 높이를 입력하세요.")
h = int(input("삼각형의 높이: "))
for i in range(1, h+1):
    print("*" * i)
print()
for i in range(h, 0, -1):
    print("*" * i) 
print()
for i in range(1, h+1):
    print(" " * (h-i) + "*" * i)
print()
for i in range(1, h+1):
    print("*" * i + " " * (h-i))
for i in range(1, h+1):
    print(" " * (h-i) + "*" * (2*i-1))
for i in range(h, 0, -1):
    print(" " * (h-i) + "*" * (2*i-1))