'''
Created on 2020. 8. 12.

@author: GDJ24
정규식!!!
'''
data = '''
    park 800805-12345678
    kim 435618-12345678
    choi 953463-64326552
'''
result = []
for line in data.split("\n") :
    word_result = []
    for word in line.split(" ") :
        if len(word) == 15 and word[:6].isdigit() and word[7:].isdigit() :
            word = word[:6] + "-" +"********"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))     

