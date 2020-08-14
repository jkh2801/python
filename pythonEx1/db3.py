'''
Created on 2020. 8. 12.

@author: GDJ24
'''
import sqlite3 # sqlite db 호출
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath) # 
cur = conn.cursor() # cursor : DB와 연결되어 명령을 전달하는 객체

while True :
    data1 = input("사용자 ID => ")
    if data1 == '' :
        break
    data2 = input("사용자 이름 => ")
    data3 = input("이메일 => ")
    data4 = input("출생 연도 => ")
    sql = "insert into usertable values('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)
    conn.commit()
cur = conn.cursor()
cur.execute("select * from usertable")
list = cur.fetchall()
for row in list : 
    print(row)
conn.close()