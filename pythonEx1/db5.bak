'''
Created on 2020. 8. 12.

@author: GDJ24
mariadb에 데이터 추가하기
'''
import pymysql #pip install pymysql (환경변수 설정)
conn = pymysql.connect(host = "localhost", port = 3306, user = "scott", passwd = "1234", db = "classdb", charset = "utf8")

try :
    cur = conn.cursor()
    data = [
        (9, "천혜향", 5000, "제주의 명물"),
        (10, "수박", 5000, "여름엔 수박이지"),
        ]
    for i in data :
        cur.execute(''' 
        insert into item (id, name, price, description) values (%s, %s, %s, %s)
        ''',i)
        cur.execute("select * from item")
    for row in cur.fetchall() :
        print(row)
finally:
    conn.rollback()
