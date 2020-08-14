'''
Created on 2020. 8. 6.

@author: GDJ24
파이썬 리스트(list) => []
    딕셔너리(자바의 Map) => {key, value}
    set => {value}
    자바에 없는 것 : 튜플
    튜플 (상수 처리된 리스트)
'''

a = [0,0,0,0]
b = []
print(a, len(a)) # [0, 0, 0, 0] 4
print(b, len(b)) # [] 0

suma, sumb = 0, 0
for i in range(0, len(a)) :
    a[i] = int(input(str(i+1) + "번째 값: "))
    suma += a[i]
    b.append(a[i])
    sumb += b[i]
print(a, len(a)) # [0, 0, 0, 0] 4
print(b, len(b)) # [] 0
print("a 리스트 합계: ", suma)
print("b 리스트 합계: ", sumb)
print(a[::-1]) # [4, 3, 2, 1]