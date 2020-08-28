'''
Created on 2020. 8. 20.

@author: GDJ24
'''
import numpy as np # python에서 수치 계산을 위한 모듈
# 수치 리스트 생성
print(np.array([1, 4, 2, 5, 3]))
print(np.array([3.14, 4, 2, 3]))
print(np.array([1, 2, 3, 4], dtype = 'float32'))

# 기본 함수
arr = np.zeros(10, dtype=int) # 10개의 요소를 0으로 채움
print(arr)
arr = np.ones((3, 5), dtype=float) # 3행 5열 리스트 생성, 1로 채움
print(arr)
arr = np.full((3,5), 3.14) # 3행 5열 리스트 생성 3.14로 채움 (지정값으로 채움)
print(arr)

# 0 ~ 20 까지의 수를 2씩 증가시킨 값을 배열 생성
arr = np.arange(0, 20, 2)
print(arr)

# 0 과 1 사이의 일정한 간격의 5개의 값을 가진 배열 생성
arr = np.linspace(0, 1, 5)
print(arr)

# 0 ~ 10 구간의 임의의 정수를 가진 3행 3열 배열 생성
arr = np.random.randint(0, 10 ,(3, 3))
print(arr)

print(arr.ndim) # 배열의 차원
print(arr.shape)
print(arr.size) # 요소의 갯수
print(arr.dtype) # 요소의 자료형