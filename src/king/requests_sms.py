#!/user/bin/env python
#encoding:utf-8

import requests
'''
r1 = requests.get('http://www.zhidaow.com') # 发送请求

print r1.status_code # 返回码 
print r1.headers['content-type'] # 返回头部信息
print r1.encoding # 编码信息
print r1.content #r.text内容部分（PS，由于编码问题，建议这里使用r.content）

'''
#获取短信验证码
mobile_list = ['15210110149','15210110149']
for i in range(len(mobile_list)):
    print i,mobile_list[i]
    payload = {'mobile': 'mobile_list[i]','position':'activity-signup'}
    r = requests.get('http://api.00bang.net/sendSmsCode/', params=payload)
    #print r.status_code
    #print r.url