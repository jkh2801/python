'''
Created on 2020. 8. 11.

@author: GDJ24
def __init__(self) 기본생성자 : 생성자를 구현하지 않으면 시스템에서 제공하는 생성자
'''
class Car :
    color = ""
    speed = 0
    #생성자 
    def __init__(self,v1="",v2=0):
        self.color = v1
        self.speed = v2
    def upSpeed(self,value):
        self.speed += value
    def downSpeed(self,value):
        self.speed -= value
myCar1 = Car() # 객체화
myCar1.color = "빨강"
myCar1.speed = 0
myCar1.upSpeed(30)
print("자동차 색상: %s, 속도: %dkm/h" % (myCar1.color,myCar1.speed))

myCar2 = Car("파랑",50)
myCar2.downSpeed(10)
print("자동차 색상: %s, 속도: %dkm/h" % (myCar2.color, myCar2.speed))

myCar3 = Car("노랑")
myCar3.downSpeed(20)
print("자동차 색상: %s, 속도: %dkm/h" % (myCar3.color, myCar3.speed))
