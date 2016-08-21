
#coding=utf-8
import xlsxwriter
import mysql.connector

config = {'host': 'wappdb008.mysql.rds.aliyuncs.com',  # 默认127.0.0.1
          'user': 'llb_db',
          'password': 'lLb_PwDa',
          'port': 3306,  # 默认即为3306
          'database': 'llb_db_official',
          'charset': 'utf8'  # 默认即为utf8
          }

conn=mysql.connector.connect(**config)
cursor=conn.cursor()

sql=('select u.create_time,u.username,ca.name,ci.city_name,case u.sex when  1 then %s else %s end as sex,'
     'u.birthday,u.mobile,case ca.check_status when 2 then %s else %s end as carCheck,pp.ppnum,pq.pqnum,r.rnum,(p.pnum+pc.pcnum) as pnum,po.enum,f.fnum,ac.cnum from user u '
     'left join ( select uc.user_id,uc.car_type_id,c.name,uc.check_status from user_vehicle_info uc,car_type c where uc.car_type_id = c.car_type_id) ca on ca.user_id = u.user_id '
     'left join ( select count(1) as pnum,user_id from praise where deleted = 0 and create_time < DATE_FORMAT(SYSDATE(),%s) group by user_id ) p on p.user_id = u.user_id '
     'left join ( select count(1) as pcnum,user_id from praise_comment where deleted = 0 and create_time < DATE_FORMAT(SYSDATE(),%s) group by user_id ) pc on pc.user_id = u.user_id '
     'left join ( select count(1) as enum,user_id from post where deleted = 0 and elite=1 and create_time < DATE_FORMAT(SYSDATE(),%s) group by user_id ) po on po.user_id = u.user_id '
     'left join ( select count(1) as fnum,a.user_id from post a,column_post_rel b where a.deleted = 0 and a.post_id = b.post_id and b.create_time < DATE_FORMAT(SYSDATE(),%s) group by a.user_id ) f on f.user_id = u.user_id '
     'left join ( select count(1) as cnum,user_id from attention_channel where channel_id in (select channel_id from channel where deleted = 0) and deleted = 0 and create_time < DATE_FORMAT(SYSDATE(),%s) group by user_id ) ac on ac.user_id = u.user_id '
     'left join ( select m.city_id,CONCAT(m.city_name,%s,n.province_name) as city_name from city m,province n where m.province_id = n.province_id) ci on ci.city_id = u.city_id '
     'left join ( select count(1) as ppnum,user_id from post where deleted = 0 and create_time < DATE_FORMAT(SYSDATE(),%s) group by user_id ) pp on pp.user_id = u.user_id '
     'left join ( select count(1) as pqnum,user_id from post where deleted = 0 and question_channel = 1 and create_time < DATE_FORMAT(SYSDATE(),%s) group by user_id ) pq on pq.user_id = u.user_id '
     'left join ( select count(1) as rnum,user_id from post_comment where deleted = 0 and create_time < DATE_FORMAT(SYSDATE(),%s) group by user_id ) r on r.user_id = u.user_id '
     'where u.status=1 and u.create_time < DATE_FORMAT(SYSDATE(),%s)')
param='%Y-%m-%d'
sxm='男'
sxw='女'
stat1='已通过'
stat2='未通过'
l='-'

cursor.execute(sql,(sxm,sxw,stat1,stat2,param,param,param,param,param,l,param,param,param,param))
data=cursor.fetchall()

workbook=xlsxwriter.Workbook('/opt/test/user.xlsx')
sheet=workbook.add_worksheet()

title=(u'注册时间',u'用户昵称',u'车型',u'城市',u'性别',u'年龄',u'手机号',u'是否认证',u'发帖数',u'问题贴',u'回复数',u'点赞数',u'精华帖',u'首页贴',u'加入社区数')
for i in range(0,len(title)):
    sheet.write(0,i,title[i])

for t in range(0,len(data)):
    for j in range(0,len(data[t])):
        if data[t][j]==None:
            if j!=5:
                sheet.write(t+1,j,0)
            else:
                continue
        else:
            sheet.write(t+1,j,data[t][j])

workbook.close()
cursor.close()
conn.close()
