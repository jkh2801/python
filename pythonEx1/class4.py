'''
Created on 2020. 8. 11.

@author: GDJ24
'''
class Line:
    length = 0
    def __init__(self,length):
        self.length = length
    # 자바의 toString 메서드 기능
    def __repr__(self):
        return "선의 길이: "+str(self.length)
    # 객체들 간의 + 연산자 상요시 호출되는 메서드 ==> 연산자 오버로딩
    def __add__(self,other):
        print("더하기 연산자가 호출되었습니다.")
        return self.length + other.length
    # 연산자 사용시 호출되는 메서드
    def __lt__(self,other):
        print("< 연산자가 호출되었습니다.")
        return self.length < other.length
    def __gt__(self,other):
        print("> 연산자가 호출되었습니다.")
        return self.length > other.length
    def __eq__(self,other):
        print("== 연산자가 호출되었습니다.")
        return self.length == other.length
    # 소멸자
    def __del__(self):
        print(self.length, "길이의 선이 제거되었습니다.")
myline1 = Line(200) # __init__ 호출, 생성자 : 객체 생성시 호출되는 메서드
myline2 = Line(100)
print(myline1) # __repr__ 호출 : 자바의 toString 메서드와 같은 기능
print(myline2)
print("두 선의 길이의 합: ",myline1+myline2)

# 두 선의 길이 비교하기
if myline1.length < myline2.length :
    print("myline2의 선이 더 깁니다.")
elif myline1.length == myline2.length :
    print("길이가 같습니다.")
else :
    print("myline1의 선이 더 깁니다.")
    
if myline1 < myline2 :
    print("myline2의 선이 더 깁니다.")
elif myline1 == myline2 :
    print("길이가 같습니다.")
else :
    print("myline1의 선이 더 깁니다.")