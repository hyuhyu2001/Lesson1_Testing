#!/user/bin/env python
#encoding:utf-8

'''
服务端一直运行一个脚本，客户端输入用户名、密码和命令，根据服务端脚本的输出给出返回结果
（1）用户名密码输入错误3次后，10分钟内不允许登陆
（2）5秒内不输入则退出
'''

import SocketServer
import os
import time
    
class MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.send('Hello, baby %s'%newline)  #给某个客户端发消息，conn是某个客户端 
        for i in range(len(l)):
            a = l[i]
            conn.send( 'enter your %s:'%a)     
            data_total= []
            while True:
                data = conn.recv(1024)
                if data != newline:
                    data_total.append(data)
                    data = ''.join(data_total)
                    if data == k[i]:
                        if i <=1:
                            conn.sendall(newline+'OK'+newline)
                        if i == 2:
                            result = getinfo('QQ.exe')
                            conn.sendall(newline+result+newline)
                            time.sleep(5)
                            conn.close()
                        break
                else:
                    data_total = []
                    conn.sendall('Wrong'+newline+'enter your %s:'%a)
                    continue
            continue
        
def getinfo(processname):
    task = os.popen('tasklist')  
    if processname in task.read():
        status = 'perfect'   
    else:
        status = 'so bad'
    return status


if __name__ == '__main__':
    l = ['username','password','command']
    k = ['jichenglong','123','ls']
    newline = os.linesep
    server = SocketServer.ThreadingTCPServer(('192.168.7.82',8020),MyServer)
    server.serve_forever()
