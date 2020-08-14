'''
Created on 2020. 8. 10.

@author: GDJ24
'''
def func1() :
    global gval
    gval = 200 # gavl 변수는 전역변수로 선언된 변수로 사용함.
    a = 20 # 지역 변수
    b = 1000
    print("func1() 함수 호출함",gval,a,b)
    
def func2() :
    b = 2000
    print("func2() 함수 호출함",gval,a,b)
    func1()
    print("전역변수 gval 값 = ",gval,a,b)
    
gval = 100 #전역 변수 (모든 함수에서 사용이 가능한 변수)
a = 10
if __name__ == '__main__' : # 프로그램의 시작
    a = 30
    func2()
    print("_main_함수 호출함",gval,a)
    
    
