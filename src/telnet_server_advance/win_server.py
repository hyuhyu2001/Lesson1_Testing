#!/user/bin/env python
#encoding:utf-8

'''
反射
task_status:send_prompt,parse_input,process_request,send_result

init_status
connected_status
get_username_status
get_password_status
get_cmd_status
quit_status

status_manger->{'connected':connected_status, 'input_user_name':get_username_status, }
stauts=connected
'''
import os
import socket
from SignIn import *
from CmdList import *

def Client_Connected():
    name = 'Hello, baby' +newline
    send_result(conn,name)    
    
def parse_input(conn,newline):
    data_total= []
    while True:
        data = conn.recv(1024)
        if data != newline:
            data_total.append(data)
            continue
        else:
            break
    data = ''.join(data_total)
    return data

def send_result(conn,name):
        conn.sendall(name)
        
def quit_status(conn):
    name = 'goodbye baby'
    send_result(conn,name)    
    conn.close()
        
def status_manger(status):
    if status == 'Connected':
        Client_Connected()
    elif status == 'username':
        get_username_status(conn,newline)   
    elif status == 'password':
        get_password_status(conn,newline)   
    elif status == 'cmd':
        get_cmd_status(conn,newline)   

def main(conn):
    status_manger('Connected')
    status_manger('username')
    status_manger('password')
    status_manger('cmd')

if __name__ == '__main__':
    newline = os.linesep
    host ='127.0.0.1'  #'192.168.7.82'
    port = 126 #8020
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#建立相关的socket对象，使用给定的地址簇，套接字类型、协议编号
    s.bind((host,port))#将套接字绑定到相关的地址
    s.listen(1)#开始监听传入连接
    conn,addr = s.accept()
    main(conn)

