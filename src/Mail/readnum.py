#coding=utf-8
#-*- coding: UTF-8 -*-
import random
import mysql.connector

config = {'host': 'wappdb008.mysql.rds.aliyuncs.com',
          'user': 'llb_db',
          'password': 'lLb_PwDa',
          'port': 3306,
          'database': 'llb_db_official',
          'charset': 'utf8'
          }
conn=mysql.connector.connect(**config)
cursor=conn.cursor()
postnum='select read_count_random from post where post_id=%s'

sqlpost='select column_post_rel.post_id from column_post_rel LEFT JOIN post on post.post_id=column_post_rel.post_id ' \
       'WHERE column_post_rel.deleted=0 and column_id=%s ORDER BY column_post_rel.create_time DESC LIMIT 1'

sql='update post set read_count_random=read_count_random+%s where post_id=%s and deleted=0'
randnum=random.randint(10,30)
colid='14fa31e806404b3898f5d1ef3378930a'
#print(randnum)
cursor.execute(sqlpost,(colid,))
postid=cursor.fetchall()[0][0]
#print(postid)
cursor.execute(postnum,(postid,))
readnum=cursor.fetchall()[0][0]
#print(readnum)
if(readnum < 50000):
    cursor.execute(sql,(randnum,postid))
    conn.commit()

cursor.close()
conn.close()