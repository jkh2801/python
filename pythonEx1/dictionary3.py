'''
Created on 2020. 8. 7.

@author: GDJ24
'''

import operator
dic,list = {},[]
dic = {"Thomas":"토마스","Edward":"애드워드","Henry":"헨리","Gothen":"고든","James":"제임스"}
list = sorted(dic.items(), key=operator.itemgetter(0), reverse=True)
# sorted : 정렬하기
# dic.items() : 내부의 튜플 객체
# operator.itemgetter(0) // 정렬의 기준을 튜플의 객체의 첫번째 정보로 하겠다. (영문이름으로 정렬)
# reverse=True : 내림차순으로 정렬
print(type(list))
print(list)
list = sorted(dic.items(), key=operator.itemgetter(1))
print(list)
