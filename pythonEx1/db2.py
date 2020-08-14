'''
Created on 2020. 8. 12.

@author: GDJ24 
화면에서 내용을 입력받아 sqlite db에 내용 저장하기
--> db3에서 이어서 작업

'''
import sqlite3 # sqlite db 호출
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath) # 
cur = conn.cursor() # cursor : DB와 연결되어 명령을 전달하는 객체


# executescript : 여러 문장을 실행
cur.executescript('''
    drop table if exists usertable;
    create table usertable (userid varchar(15) primary key,
    username varchar(20),
    email varchar(30),
    year integer);
    
''')
