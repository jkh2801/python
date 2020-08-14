'''
Created on 2020. 8. 11.

@author: GDJ24
'''
class Car :
    color = ""
    speed = 0
    num = 0
    count = 0
    #생성자 
    def __init__(self):
        self.speed = 0 # 인스턴스 변수
        Car.count += 1 # 클래스 변수
        self.num = Car.count # 인스턴스 변수
    def printMessage(self):
        print("색상:%s, 속도:%dkm/h, 번호:%d, 생산번호:%d" % (self.color,self.speed,self.num, Car.count))
        
mycar1, mycar2 = None, None
mycar1 = Car() # 객체화
mycar1.speed = 30
mycar1.printMessage()
print()
mycar2 = Car() # 객체화
mycar2.speed = 50
mycar2.printMessage()
print()
print("생산번호: %d" % (mycar1.count))

