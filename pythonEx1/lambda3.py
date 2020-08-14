'''
Created on 2020. 8. 10.

@author: GDJ24
'''
mylist = [1, 2, 3, 4, 5]
#map을 이용하여 mylist 각각의 값을 10 더하기
add = lambda num : num + 10
mylist = list(map(add, mylist))
print(mylist)

mylist = list(map((lambda num : (num-10) * 10), mylist))
print(mylist)

list1 = [1,2,3,4]
list2 = [10,20,30,40]
hap = lambda a,b : a+b
haplist = list(map(hap, list1, list2))
print(haplist)

hap = lambda a,b,c : a+b+c
haplist = list(map(hap, mylist, list1, list2))
print(haplist)
print(mylist)