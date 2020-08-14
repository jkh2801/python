'''
Created on 2020. 8. 12.

@author: GDJ24
추상클래스 : 선언부만 존재하는 클래스 
Python의 추상클래스는 객체화가 된다. // 단, 오버라이딩이 된 메서드만 호출 가능은 동일
Java의 경우 객체화가 안된다.
'''
class SuperClass : 
    def method(self): # 추상메서드 
        raise NotImplementedError # 자손클래스에서 오버라이딩을 해야 한다.
class SubClass1(SuperClass):
    def method(self):
        print("SubClass1 에서 Method()를 오버라이딩 함")
class SubClass2(SuperClass):
    def method(self):
        print("SubClass2 에서 Method()를 오버라이딩 함")
        
sub1 = SubClass1()
sub2 = SubClass2()
sub1.method()
sub2.method()