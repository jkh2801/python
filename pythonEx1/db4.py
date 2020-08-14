'''
Created on 2020. 8. 12.

@author: GDJ24
mariadb 사용
'''
import pymysql #pip install pymysql (환경변수 설정)
conn = pymysql.connect(host = "localhost", port = 3306, user = "scott", passwd = "1234", db = "classdb", charset = "utf8")

try :
    cur = conn.cursor()
    cur.execute("select * from item")
#     for row in cur.fetchall() :
#         print(row[0],row[1],row[2])
#         print(row)
    while True :
        row = cur.fetchone() # 1개만 레코드만 조회
        if row == None : #조회된 레코드가 없다면    
            break
        print(row)
finally:
    cur.close() 
    conn.close()
