'''
Created on 2020. 8. 10.

@author: GDJ24
1. 리턴값을 2개 이상의 경우 => List로 반환
2. 가변 매개변수 함수
'''
def multi(a,b) :
    list= []
    res1 = a + b
    res2 = a - b
    list.append(res1)
    list.append(res2)
    return list

def multiParm(* p) :
    result = 0
    for i in p:
        result += i
    return result


list = []
hap, sub = 0, 0
list = multi(100, 200)
hap = list[0]
sub = list[1]
print("multi 함수의 리턴: %d, %d" % (hap, sub))

print("multiParm(10) = ",multiParm(10))
print("multiParm(10, 20) = ",multiParm(10, 20))
print("multiParm(10, 20, 30) = ",multiParm(10, 20, 30))
print("multiParm(10, 20, 30, 40) = ",multiParm(10, 20, 30, 40))

''' 피보나치 수열 출력하기 '''
def fibo(n) :
    for i in range(2, n) :
        list.append(list[i-2] + list[i-1])
    return list
    
list = []
list.append(1)
list.append(1)
num = int(input("피보나치 수열의 요수 갯수를 입력하세요(3이상의 값) : "))
print("f(",num,")=",end="")
print(fibo(num))