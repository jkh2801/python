'''
Created on 2020. 8. 7.
tuple : 변경불가 리스트
@author: GDJ24
'''
tp1 = (10, 20, 30)
print(tp1)
print(tp1[0],tp1[1],tp1[2])

# 리스트로 변경 후 수정이 가능하다.
list = list(tp1)
list.append(40)
list[0] = 100
print(list)
tp1 = tuple(list)
print(tp1)
print("tp1의 크기: ",len(tp1),", list의 크기: ",len(list))
print("tp1[1:3]: ",tp1[1:3],", list[1:3]: ",list[1:3])
print("tp1[:3]: ",tp1[:3],", list[:3]: ",list[:3])
print("tp1[2:]: ",tp1[2:],", list[2:]: ",list[2:])
print("tp1[::2]: ",tp1[::2],", list[::2]: ",list[::2])
