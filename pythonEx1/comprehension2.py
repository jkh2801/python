'''
Created on 2020. 8. 11.

@author: GDJ24
{} 은 set으로 해석
[] 은 list
() 은 tuple
'''
set1 = {x**2 for x in [1,1,2,2,3,3]}
print(set1)

list1 = [x**2 for x in [1,1,2,2,3,3]]
print(list1)

# 1부터 10까지의 수 중 짝수의 제곱을 출려하기
print([x**2 for x in range(1,11) if x % 2 == 0])
print(sorted(list1))