#!/user/bin/env python
#encoding:utf-8

from win_server import *

l = ['username','password']
k = ['jichenglong','jcl123456']
      
def get_username_status(status,conn,newline):
    #status = 'username'
    while True:
        name = 'enter your %s:'%l[0]
        send_result(status,conn,name)
        data = parse_input(conn,newline)
        if data == k[0]:
            name = '%s is ok'%l[0]+newline
            send_result(status,conn,name)
            break
        else:
            name = '%s is Wrong'%l[0]+newline
            send_result(status,conn,name)
            continue

def get_password_status(status,conn,newline):
    #status = 'password'
    while True:
        name = 'enter your %s:'%l[1]
        send_result(status,conn,name)
        data = parse_input(conn,newline)
        if data == k[1]:
            name = '%s is OK'%l[1]+newline
            send_result(status,conn,name)
            break
        else:
            name = '%s is Wrong'%l[1]+newline
            send_result(status,conn,name)
            continue


