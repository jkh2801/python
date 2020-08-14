'''
Created on 2020. 8. 13.

@author: GDJ24
'''
import re # 정규식 사용을 위한 모듈

str = "The quick brown fox jumps over the lazy dog"
str_list = str.split()
pattern = re.compile("Th+e")
count = 0
for word in str_list :
    if pattern.search(word) : # pattern에 맞는 문자가 있는냐
        count += 1
print("output 1 : {1:s}:{0:d}".format(count, "갯수"))

#re.I : 대소문자 구분 없이
pattern = re.compile("Th*e",re.I)
count = 0
for word in str_list :
    if pattern.search(word) : # pattern에 맞는 문자가 있는냐
        count += 1
print("output 2 : {1:s}:{0:d}".format(count, "갯수"))

pattern = re.compile("(?P<match_word>Th*e)",re.I)
count = 0
print("output 3 :",end=" ")
for word in str_list :
    if pattern.search(word) : # pattern에 맞는 문자가 있는냐
        print("{0}".format(pattern.search(word).group("match_word")),end=",")
print()

str_find = "The"        
pattern = re.compile(str_find,re.I)
print("output 4 : {0}".format(pattern.sub("a",str)))
