#!/user/bin/env python
#encoding:utf-8

import xlsxwriter
import mysql.connector
import time

config = {'host': 'wappdb008.mysql.rds.aliyuncs.com',
          'user': 'llb_db',
          'password': 'lLb_PwDa',
          'port': 3306,
          'database': 'llb_db_official',
          'charset': 'utf8'
          }

conn=mysql.connector.connect(**config)
cursor=conn.cursor()


sql=('select u.username,p.create_time,c.channel_name,p.question_channel,k.title as title,p.content,pp.pnum,pc.cnum,p.read_count, p.elite,cc.topPost as topPost,b.recommendPost as recommendPost,  d.notiPost as notiPost from post p '
     'LEFT JOIN (select post_id, COUNT(post_id) as recommendPost from column_post_rel where deleted = 0 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) b on p.post_id = b.post_id ' \
     'LEFT JOIN (select post_id, COUNT(post_id) as topPost from post_operate where deleted = 0 and opera_type = 1 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) cc on p.post_id = cc.post_id ' \
     'LEFT JOIN (select post_id, COUNT(post_id) as notiPost from post_operate where deleted = 0 and opera_type = 0 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) d on p.post_id = d.post_id ' \
     'LEFT JOIN ( select f.post_id,f.title from (select post_id,title from post_operate  where deleted = 0 and post_id not in ' \
      '(select post_id from column_post_rel where create_time< DATE_FORMAT(sysdate(),%s) ) UNION select post_id,title from column_post_rel where deleted = 0 and create_time< DATE_FORMAT(sysdate(),%s)) f ) k ON p.post_id = k.post_id ' \
      'left join channel c on p.channel_id = c.channel_id ' \
      'left join user u on p.user_id = u.user_id ' \
      'left join (select post_id, COUNT(1) as pnum from praise where deleted = 0 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) pp on p.post_id = pp.post_id ' \
      'left join (select post_id, COUNT(1) as cnum from post_comment where deleted = 0 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) pc on p.post_id = pc.post_id ' \
      'where p.deleted = 0 and c.deleted=0 and p.create_time< DATE_FORMAT(sysdate(),%s) ' \
      'and p.post_id not in (select f.post_id from forbidden f where f.deleted = false and (f.expire_time > now() or f.expire_time is null) ' \
      'and f.post_id is not null) and c.channel_name!="深夜魅影" and u.username not in ("只爱老婆","秋叶","生活之旅","汪洋大海","纯爷们","金少主","三少爷","开跑车的大海龟","王小贱","千手屠夫","小菱菱") order by p.create_time desc')

sqlsome=('select u.username,p.create_time,c.channel_name,p.question_channel,k.title as title,p.content,pp.pnum,pc.cnum,p.read_count, p.elite,cc.topPost as topPost,b.recommendPost as recommendPost,  d.notiPost as notiPost from post p '
     'LEFT JOIN (select post_id, COUNT(post_id) as recommendPost from column_post_rel where deleted = 0 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) b on p.post_id = b.post_id ' \
     'LEFT JOIN (select post_id, COUNT(post_id) as topPost from post_operate where deleted = 0 and opera_type = 1 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) cc on p.post_id = cc.post_id ' \
     'LEFT JOIN (select post_id, COUNT(post_id) as notiPost from post_operate where deleted = 0 and opera_type = 0 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) d on p.post_id = d.post_id ' \
     'LEFT JOIN ( select f.post_id,f.title from (select post_id,title from post_operate  where deleted = 0 and post_id not in ' \
      '(select post_id from column_post_rel where create_time< DATE_FORMAT(sysdate(),%s) ) UNION select post_id,title from column_post_rel where deleted = 0 and create_time< DATE_FORMAT(sysdate(),%s)) f ) k ON p.post_id = k.post_id ' \
      'left join channel c on p.channel_id = c.channel_id ' \
      'left join user u on p.user_id = u.user_id ' \
      'left join (select post_id, COUNT(1) as pnum from praise where deleted = 0 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) pp on p.post_id = pp.post_id ' \
      'left join (select post_id, COUNT(1) as cnum from post_comment where deleted = 0 and create_time< DATE_FORMAT(sysdate(),%s) GROUP BY post_id) pc on p.post_id = pc.post_id ' \
      'where p.deleted = 0 and c.deleted=0 and p.create_time< DATE_FORMAT(sysdate(),%s) ' \
      'and p.post_id not in (select f.post_id from forbidden f where f.deleted = false and (f.expire_time > now() or f.expire_time is null) ' \
      'and f.post_id is not null) and u.username in ("只爱老婆","秋叶","生活之旅","汪洋大海","纯爷们","金少主","三少爷","开跑车的大海龟","王小贱","千手屠夫","小菱菱") order by p.create_time desc')

sqluser=('select u.create_time,u.username,ca.name,ci.city_name,case u.sex when  1 then %s else %s end as sex,'
     'u.birthday,u.mobile,case ca.check_status when 2 then %s else %s end as carCheck,pp.ppnum,pq.pqnum,r.rnum,(p.pnum+pc.pcnum) as pnum,po.enum,f.fnum,ac.cnum,praise_count from user u '
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

cursor.execute(sql,(param,param,param,param,param,param,param,param))
data=cursor.fetchall()

tim=time.strftime('%Y-%m-%d',time.localtime(time.time()))
location='/opt/test/postall/'+'post'+tim+'.xlsx'
workbook=xlsxwriter.Workbook(location)
sheet=workbook.add_worksheet(u"帖子信息")
sheet1=workbook.add_worksheet(u"水号")
sheet2=workbook.add_worksheet(u"用户信息")
sheet3=workbook.add_worksheet(u"4S店预约信息")
sheet4=workbook.add_worksheet(u"迪士尼中奖名单")

title=(u'用户名',u'创建日期',u'社区名',u'是否问题贴',u'帖子标题',u'帖子内容',u'点赞总数',u'回复总数',u'真实围观数',u'是否精华',u'是否置顶',u'是否推荐首页',u'是否公告')
for i in range(0,len(title)):
    sheet.write(0,i,title[i])

for t in range(0,len(data)):
    for j in range(0,len(data[t])):
        if data[t][j]==None:
            sheet.write(t+1,j,0)
        else:
            sheet.write(t+1,j,data[t][j])

cursor.execute(sqlsome,(param,param,param,param,param,param,param,param))
data1=cursor.fetchall()

for i in range(0,len(title)):
    sheet1.write(0,i,title[i])

for t in range(0,len(data1)):
    for j in range(0,len(data1[t])):
        if data1[t][j]==None:
            sheet1.write(t+1,j,0)
        else:
            sheet1.write(t+1,j,data1[t][j])

cursor.execute(sqluser,(sxm,sxw,stat1,stat2,param,param,param,param,param,l,param,param,param,param))
data2=cursor.fetchall()

title2=(u'注册时间',u'用户昵称',u'车型',u'城市',u'性别',u'年龄',u'手机号',u'是否认证',u'发帖数',u'问题贴',u'回复数',u'点赞数',u'精华帖',u'首页贴',u'加入社区数',u'获赞数')
for i in range(0,len(title2)):
    sheet2.write(0,i,title2[i])

for t in range(0,len(data2)):
    for j in range(0,len(data2[t])):
        if data2[t][j]==None:
            if j!=5:
                sheet2.write(t+1,j,0)
            else:
                continue
        else:
            sheet2.write(t+1,j,data2[t][j])
            
cursor.execute('SELECT  k.create_time,k.phone,k.name,k.cartype,p.ks_province_name,c.ks_city_name,k.dealer,si.full_name FROM  llb_activity.ks_reservation  k, llb_db_official.city  c ,llb_db_official.province  p , llb_db_official.shop_info si WHERE  si.ks_shop_id=k.dealer AND  si.deleted=0 AND   c.ks_city_id=k.city AND  p.ks_province_id=k.province  AND DATE(k.create_time)=(SELECT DATE_SUB(CURDATE(),INTERVAL 1 DAY))  GROUP BY k.phone ORDER BY k.create_time DESC ')
data3=cursor.fetchall()

title3=(u'预约试驾',u'手机号',u'用户昵称',u'预约车型',u'省',u'市',u'供应商编号',u'供应商名称')
for i in range(0,len(title3)):
    sheet3.write(0,i,title3[i])

for t in range(0,len(data3)):
    for j in range(0,len(data3[t])):
        if data3[t][j]==None:
            if j!=5:
                sheet3.write(t+1,j,0)
            else:
                continue
        else:
            sheet3.write(t+1,j,data3[t][j])

cursor.execute('SELECT  activity_id,mobile FROM  llb_activity.activity_take_record WHERE prize_flag = 1')
data4=cursor.fetchall()

title4=(u'迪士尼活动期数',u'手机号')
for i in range(0,len(title4)):
    sheet4.write(0,i,title4[i])

for t in range(0,len(data4)):
    for j in range(0,len(data4[t])):
        if data4[t][j]==None:
            if j!=5:
                sheet4.write(t+1,j,0)
            else:
                continue
        else:
            sheet4.write(t+1,j,data4[t][j])
            
workbook.close()
cursor.close()
conn.close()

