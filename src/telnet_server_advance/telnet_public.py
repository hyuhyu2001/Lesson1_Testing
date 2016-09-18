#!/user/bin/env python
#encoding:utf-8

from win_server import *

def Client_Connected(conn,newline):
    status = 'Connected'
    name = newline
    send_result(status,conn,name)

    
def parse_input(conn,newline):
    data_total= []
    while True:
        data = conn.recv(1024)
        if not len(data):
            break
        elif data != newline:
            data_total.append(data)
            continue
        else:
            break
    data = ''.join(data_total)
    return data

def send_result(status,conn,name):
    if status == 'Connected':
        conn.send("GET / HTTP/1.1"+name)
        conn.send("Accept:text/html,application/xhtml+xml,*/*;q=0.8"+name)
        conn.send("Accept-Language:zh-CN,zh;q=0.8,en;q=0.6"+name)
        conn.send("Cache-Control:max-age=0"+name)
        conn.send("Connection:Close"+name+name) #keep-alive
    else:
        conn.send(name)
        
def quit_status(conn):
    name = 'goodbye baby'
    send_result(conn,name)    
    conn.close()
        