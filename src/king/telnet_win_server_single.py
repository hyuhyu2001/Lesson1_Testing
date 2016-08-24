#!/user/bin/env python
#encoding:utf-8

import socket

#设置IP地址及端口

def send_data(conn):
    conn.send("HTTP/1.1 200 OK\r\n\r\n") #给某个客户端发消息，conn是某个客户端
    conn.send("Hello, baby \r\n\r\n") #给客户端发消息
    flag = True
    while flag:
        conn.send("please enter your username:") #给客户端发消息
        data = conn.recv(1024)
        if len(data.strip()) == 0:   #如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
            conn.sendall('Done.')
        elif data == '0':
            print 'Client Send：',repr(data)
            conn.sendall('\r\n'+'OK'+'\r\n')
        else:
            conn.sendall('\r\n'+'wrong'+'\r\n')

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#建立相关的socket对象，使用给定的地址簇，套接字类型、协议编号
    s.bind((host,port))#将套接字绑定到相关的地址
    s.listen(1)#开始监听传入连接
    
    conn,addr = s.accept()
    print 'Connected by：',addr

    send_data(conn) #调用发送数据的接口，给客户端返回数据

    conn.close()
    
if __name__ == '__main__': #01 如果是主函数，执行main函数
    host = '127.0.0.1'
    port = 126
    main()