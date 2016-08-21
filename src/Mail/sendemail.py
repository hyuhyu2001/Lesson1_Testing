#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from email import encoders

mail_host='smtp.exmail.qq.com'
mail_user='xiongping@cloud-young.com'
mail_pass='Xiongping1'

sender='xiongping@cloud-young.com'
receivers=['yanxt@cloud-young.com','xiongping@cloud-young.com','liuyc@cloud-young.com']

message=MIMEMultipart()
message['From']=sender
message['To'] =  ",".join(receivers)
subject = '帖子和用户数据'
message['Subject'] = Header(subject, 'utf-8')
message.attach(MIMEText('帖子和用户数据日常统计，具体见附件','plain','utf-8'))
with open('/opt/test/post.xlsx','rb') as f:
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(f.read())
    att.add_header('Content-Disposition', 'attachment', filename="日常数据.xlsx")
    encoders.encode_base64(att)
    message.attach(att)

t=0
while(1):
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
    print "发送成功"
        t=0
    except smtplib.SMTPException:
        t=1
        print "Error: 发送失败"
    if t!=0:
        continue
    else:
        break
