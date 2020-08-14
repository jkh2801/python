'''
Created on 2020. 8. 5.

@author: GDJ24
'''
print("초를 입력하세요.")
sec = int(input("몇 초 입니까?"))
hr = sec//3600
mm = sec%3600//60
ss = sec%60
print("%d시간 %d분 %d초" %(hr,mm,ss))
