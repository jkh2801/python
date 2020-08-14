'''
Created on 2020. 8. 12.

@author: GDJ24
'''
import sqlite3 # sqlite db 호출
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath) # 
cur = conn.cursor() # cursor : DB와 연결되어 명령을 전달하는 객체


# executescript : 여러 문장을 실행
cur.executescript('''
    drop table if exists items;
    create table items (item_id integer primary key,
    name text unique,
    price integer);
    insert into items(name, price) values ("Apple",800);
    insert into items(name, price) values ("Orange",500);
    insert into items(name, price) values ("Kiwi",300);
''')
conn.commit() # Transaction 완료, 정상처리 / rollback() : 취소
cur = conn.cursor()
cur.execute("select * from items")
item_list = cur.fetchall()
print(type(item_list))
for i in item_list :
    print(i)