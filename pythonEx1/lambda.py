'''
Created on 2020. 8. 10.

@author: GDJ24
'''
def hap (a,b) :
    res = a + b
    return res
print(hap(10, 20))

#람다식 방식으로 구현
hap1 = lambda a,b : a+b
print(hap1(10,20))
hap1 = lambda a,b : a*b
print(hap1(10,20))

# 매개변수 초기화 하기
hap2 = lambda a = 0, b = 1 : a+b
print(hap2())
print(hap2(100))
print(hap2(100,200))