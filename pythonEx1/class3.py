'''
Created on 2020. 8. 11.

@author: GDJ24
python은 다중상속이 가능하다.
'''
class Car :
    speed = 0
    door = 3
    def upSpeed(self, value) :
        self.speed += value
        print("현재 속도(부모클래스): %d" % self.speed)
class Sedan(Car): # 상속표현
    pass # 추가 멤버가 없음을 표시
class Truck(Car):
    def upSpeed(self,value): # 오버라이딩
        self.speed += value
        if self.speed > 150 :
            self.speed = 150
        print("현재 속도(자손클래스): %d" % self.speed)
    
class Container :
    room = 1
class MovingCar(Container, Car): # 다중 상속
    pass

sedan1 = Sedan()
truck1 = Truck()
print("트럭: ",end="")
truck1.upSpeed(200)
print("승용차: ",end="")
sedan1.upSpeed(200)
mcar = MovingCar()
mcar.upSpeed(60)
print("이동차량의 방갯수: ",mcar.room,", 문의 갯수: ",mcar.door)
