'''
Created on 2020. 8. 5.

@author: GDJ24
'''
print("금액을 입력하세요.")
money = int(input("금액: "))
print("500원: ",(money//500),"개")
print("100원: ",(money%500//100),"개")
print("50원: ",(money%100//50),"개")
print("10원: ",(money%50//10),"개")
print("5원: ",(money%10//5),"개")
print("1원: ",(money%5),"개")