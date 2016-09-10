#!/user/bin/env python
#encoding:utf-8

'''
添加守护进程
服务端一直运行一个脚本，客户端输入用户名、密码和命令，根据服务端脚本的输出给出返回结果
（1）用户名密码输入错误3次后，10分钟内不允许登陆
（2）5秒内不输入则退出
'''

import SocketServer
import os
import time
import sys


def daemonize(stdin = '/dev/null',stdout = '/dev/null',stderr = '/dev/null'):
    #重定向标准文件描述（默认情况下定向到/dev/null）
    try:
        pid = os.fork()
        #父进程（会话组头领进程）退出，这意味着一个非会话组头领永远不能重新获得控制终端
        if pid >0:
            sys.exit()  #父进程退出
    except OSError,e:
        sys.stderr.write("fork #1 failed: (%d) %s\n")%(e.errno,e.strerror)
        sys.exit(1)
    #从母体环境脱离
    os.chdir("/") #chdir确认进程不保持任何目录于使用状态，否则不能umount一个文件系统。也可以改变到对于守护程序运行重要的文件所在目录
    os.umask(0) #调用umask(0)以便拥有对于写的任何东西的完全控制，因为有时不知道继承了什么样的umask
    os.setsid()  #setsid调用成功后，进程成为新的会话组长和新的进程组长，并与原来的登录会话和进程组脱离。  
    #执行第二次fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) #第二个父进程退出
    except OSError,e:
        sys.stderr.write("fork #2 failed: (%d) %s\n")%(e.errno,e.strerror)
        sys.exit(1)
        
    #进程已经是守护进程了，重定向标准文件描述
    for f in sys.stdout,sys.stderr:f.flush()
    si = open(stdin,'r')
    so = open(stdout,'a+')
    se = open(stderr,'a+',0) 
    os.dup2(si.fileno(), sys.stdin.fileno()) #dup2函数原子化关闭和复制文件描述符
    os.dup2(so.fileno(), sys.stdout.fileno())  
    os.dup2(se.fileno(), sys.stderr.fileno())  
    
class MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall('Hello, baby %s'%newline)  #给某个客户端发消息，conn是某个客户端 
        for i in range(len(l)):
            a = l[i]
            conn.send( 'enter your %s:'%a)     
            data_total= []
            while True:
                data = conn.recv(8096)
                if data != newline:
                    data_total.append(data)
                    data = ''.join(data_total)
                    if data == k[i]:
                        if i <=1:
                            conn.sendall(newline+'OK'+newline)
                        if i == 2:
                            result = getinfo('sh')
                            conn.sendall(newline+result+newline)
                            time.sleep(5)
                            conn.close()
                        break
                else:
                    data_total = []
                    conn.sendall('NO'+newline+'enter your %s:'%a)
                    continue
            continue
        
def getinfo(processname):
    task = os.popen('sh /usr/local/tomcat_h5_test/bin/startup.sh')  
    if 'success' in task.readlines():
        status = 'perfect'   
    else:
        status = 'so bad'
    return status


if __name__ == '__main__':
    daemonize('/dev/null','/home/jinzj/telnet_server_stdout.log','/home/jinzj/telnet_server_error.log')  
    l = ['username','password','command']
    k = ['jichenglong','123','sh']
    newline = os.linesep
    server = SocketServer.ThreadingTCPServer(('192.168.7.82',8020),MyServer)
    server.serve_forever()
