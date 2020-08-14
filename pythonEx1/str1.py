'''
Created on 2020. 8. 6.

@author: GDJ24
'''
print("안녕하세요")
print("안녕하세요"[0]) #안
print("안녕하세요"[-1]) #요
print("안녕하세요"[-2]) #세

print("안녕하세요"[1:3]) #녕하 1 ~ 2까지 출력
print("안녕하세요"[:3]) #안녕하 0 ~ 2까지 출력
print("안녕하세요"[1:]) #녕하세요 1 ~ 끝까지 출력
print("안녕하세요"[::2]) #안하요 처음부터 2칸씩 출력
print("안녕하세요"[::-1]) #요세하녕안 역순으로 1칸씩 출력
print("안녕하세요"[::-2]) #요하안 역순으로 2칸씩 출력

print(type("안녕하세요")) # 자료형 
print(len("안녕하세요")) #5 문자열의 길이

a = "helloa"
cnt = 0;
for i in range(0,len(a)) :
    if(a[i] == 'l') :
        cnt += 1
print("l 문자의 겻수=",cnt) #2
print("l 문자의 갯수=",a.count('l')) #2
print("l 문자의 위치=",a.find('l')) #2
print("a 문자의 위치=",a.find('a')) #5
print("l 문자의 위치=",a.index('l')) #2
print("a 문자의 위치=",a.index('a')) #5