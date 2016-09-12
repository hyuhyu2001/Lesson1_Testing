#!/user/bin/env python
#encoding:utf-8

import win_server as w

l = ['username','password']
k = ['jichenglong','jcl123456']
    
def get_username_status(conn,newline):
    while True:
        name = 'enter your %s:'%l[0]
        w.send_result(conn,name)
        data = w.parse_input(conn,newline)
        if data == k[0]:
            name = '%s is OK'%l[0]+newline
            w.send_result(conn,name)
            break
        else:
            name = '%s is Wrong'%l[0]+newline
            w.send_result(conn,name)
            continue


def get_password_status(conn,newline):
    while True:
        name = 'enter your %s:'%l[1]
        w.send_result(conn,name)
        data = w.parse_input(conn,newline)
        if data == k[1]:
            name = '%s is OK'%l[1]+newline
            w.send_result(conn,name)
            break
        else:
            name = '%s is Wrong'%l[1]+newline
            w.send_result(conn,name)
            continue


