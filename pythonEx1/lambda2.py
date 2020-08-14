'''
Created on 2020. 8. 10.

@author: GDJ24
'''
myList = [1,2,3,4,5]

def add10(num):
    return num + 10
for i in range(len(myList)) : 
    # myList[i] = add(myList[i])
    myList[i] = (lambda num: num+10) (myList[i])
print(myList)