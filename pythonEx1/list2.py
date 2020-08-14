'''
Created on 2020. 8. 6.

@author: GDJ24
'''
aa, bb = [], []
for i in range (0, 40) :
    if(i % 2 == 0 ) :
        aa.append(i)
print(aa)
bb = aa[::-1]
print(bb)