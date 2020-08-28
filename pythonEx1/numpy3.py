'''
Created on 2020. 8. 20.

@author: GDJ24
'''
import numpy as np
# 0부터 9까지 임이의 난수 10개를 배열로 저장
x = np.random.randint(10, size = 10)
x_sub = x[:2]
print(x)
print(x_sub)
x_sub[0] = 20 # 사본(x_sub)의 0번재 요소를 20으로 바꾸면 원본 (x)로 바뀐다.
print(x)
print(x_sub)

# 배열 복사
x_cop = x.copy()
x_cop[0] = 100
print(x)
print(x_cop)

# 배열의 재편성
x2 = x.reshape(5,2)
print(x2)

# 0부터 9까지의 임의의 수를 9개를 가지고 잇는 배열 a
# a배열을 3행 3열로 배열로 재편성
a = np.random.randint(10, size = 9)
a = a.reshape(3,3)
print(a)