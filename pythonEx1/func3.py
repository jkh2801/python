'''
Created on 2020. 8. 7.

@author: GDJ24
'''
def calc(a, b, c) :
    if c == "+" :
        return a+b
    elif c == "-" :
        return a-b
    elif c == "*" :
        return a*b
    elif c == "/" :
        return a//b
    

oper = input("연산자를 선택하세요. (+, -, *, /)")
var1 = int(input("첫번째 수를 입력하세요."))
var2 = int(input("두번째 수를 입력하세요."))
res = calc(var1, var2, oper)
print("계산: %d %s %d = %d" % (var1, oper, var2, res))