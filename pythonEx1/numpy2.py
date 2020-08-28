'''
Created on 2020. 8. 20.

@author: GDJ24
'''
import numpy as np
x = np.arange(10) # 0 ~ 9로 이루어지 ㄴ배열
print(x)
print(x[:5])
print(x[5:])
print(x[4:7])
print(x[::2])
print(x[1::2])
print(x[1:8:3])
print(x[::-1])

# 0 부터 9 까지의 난수를 4행 5열에 저장
x = np.random.randint(10, size = (4,5))
print(x)
print(x[:2,:3])
print(x[:,::2])
print(x)
print(x[::-1,::-1])