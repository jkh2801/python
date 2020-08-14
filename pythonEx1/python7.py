'''
Created on 2020. 8. 5.

@author: GDJ24
'''
num = 0
while num < 5 :
    print(num,end=",")
    num += 1
print("\nfor 구문")
# range(0,5) 0부터 4까지
for i in range(0,5) :
    print(i,end=",")
    
#1부터 100까지의 합 구하기
sum = esum = osum = 0
for i in range(1, 101) :
    sum += i
    if(i%2==0) :
        esum += i
    else :
        osum += i
print("\n1부터 100까지의 합:",sum)
print("\n1부터 100까지의 짝수합:",esum)
print("\n1부터 100까지의 홀수합:",osum)