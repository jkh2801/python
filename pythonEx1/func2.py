'''
Created on 2020. 8. 7.

@author: GDJ24
'''
def getSum(l) :
    sum = 0
    for i in range(0, len(list)) :
        sum += list[i]
    return sum()
    
    
def getMean(l) :
    sum = 0
    for i in range(0, len(list)) :
        sum += list[i]
    return sum/len(list)   
    
    
list = [2,3,3,4,4,5,5,6,6,8,8]
print("list의 값의 합: ",getSum(list))
print("list값의 평균: ",getMean(list))

tp = (2,3,3,4,4,5,5,6,6,8,8)
print("tp의 값의 합: ",getSum(tp))
print("tp값의 평균: ",getMean(tp))