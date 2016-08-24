#!/user/bin/env python
#encoding:utf-8

'''
本机运行脚本，监听本机telnet客户端发来的数据
telnet端口已由23改为126
'''

import socket

#设置客户端的IP地址及服务器的端口
host = '127.0.0.1'
port = 126

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#建立相关的socket对象，使用给定的地址簇，套接字类型、协议编号
s.bind((host,port))#将套接字绑定到相关的地址
s.listen(1)#开始监听传入连接

conn,addr = s.accept() #接受TCP连接，并返回新的套接字与IP地址
print '连接过来的IP地址是：',addr

while 1:
    data = conn.recv(1024)  #把接收的数据实例化
    if not data:
        break
    print '客户端发送来的数据是：',repr(data)#接收客户端发来的数据
    conn.sendall(data.upper()) #将数据转换为大写，返回数据到客户端
conn.close()