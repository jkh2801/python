'''
Created on 2020. 8. 7.

@author: GDJ24
dictionary : key : value 구조
tuple : 변경 불가 리스트 // 괄호로 표현된다.
'''

singer = {}
singer['이름'] = '트와이스'
singer['구성원수'] = 9
singer['데뷔곡'] ="우아하게"
singer['소속사'] = 'JYP'

for i in singer.keys() :
    print("%s => %s" % (i, singer[i]))
print(singer)
print(singer['이름'])
print(type(singer))
print(str(list(singer.keys()))+"*****")
print(str(list(singer.values())))
print(list(singer.items()))
print(str(len(singer)))


foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","맥주":"치킨"}
for i in foods.keys() :
    print("%s => %s" % (i, foods[i]))
    
# 화면에서 음식을 입력받아 궁합음식 출력하기
while True :
    myfood = input(str(list(foods.keys())) + "중 음식이름을 입력하세요.")
    if myfood in foods :
        print(myfood + "와 어울리는 음식은 "+foods[myfood] + " 입니다.")
    elif(myfood == "종료") :
        print(list(foods.items()))
        break
    else :
        print("관련 데이터가 없습니다.")
        yn = input("좋아하는 음식으로 등록하시겠숩니까? (y)")
        if yn == 'y' or yn == 'Y' :
            f = input("궁합읍식을 입력하세요.")
            foods[myfood] = f
    
    