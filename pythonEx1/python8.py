'''
Created on 2020. 8. 5.

@author: GDJ24
'''
print("숫자를 입력하세요")
num = int(input("num: "))+1
sum = esum = osum = 0
for i in range(1, num) :
    sum += i
    if(i%2==0) :
        esum += i
    else :
        osum += i
print("\n1부터 100까지의 합:",sum)
print("\n1부터 100까지의 짝수합:",esum)
print("\n1부터 100까지의 홀수합:",osum)