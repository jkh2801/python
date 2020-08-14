'''
Created on 2020. 8. 6.

@author: GDJ24
'''
i,j = 0,0
for i in range(2, 10) :
    print("%5d단" % i, end="\t\t")
print()
for i in range(2, 10) :
    for j in range(2, 10) :
        print("%2d X %2d = %3d" % (j,i,(i*j)), end="\t")
    print()
    