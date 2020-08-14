'''
Created on 2020. 8. 7.

@author: GDJ24
'''
country = {"대한민국":"서울","영국":"런던","중국":"베이징","미국":"워싱턴","대만":"타이페이"}
while True :
    w = input(str(list(country.keys())) + "중에서 나라를 입력하세요.")
    if w in country.keys() :
        print(w +"의 수도는 " + country[w] +" 입니다.")
    elif w == '종료' :
        print(list(country.items()))
        break
    else :
        print("해당 데이터가 없습니다.")
        a = input("등록하시겠습니까? (y)")
        if a == 'y' or a =='Y' :
            b = input("나라의 수도를 입력하세요.")
            country[w] = b
            