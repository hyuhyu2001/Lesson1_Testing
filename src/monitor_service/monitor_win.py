#!/user/bin/env python
#encoding:utf-8


'''
监控windows某服务和进程状态
'''
import os
import time

#如果pid不存在了，service肯定stop
def getinfo(processname):
    task = os.popen('tasklist')  #打开cmd，执行tasklist命令，查看本机所有进程
    if processname in task.read(): #判断进程是否打开
        try:
            num = os.popen('tasklist').read().split().index(processname) #得到processname的index
            tasklist = os.popen('tasklist').read().split() #分割成列表
            index_n = num +1 
            pid = int(tasklist[index_n])  #得到进程的进程号
            time1 = time.ctime() 
            status = 1
        except Exception,e:
            print e
            status = 0   # 0 代表进程停止
            pid = 0
            time1 = time.ctime()
    else:
        print '''Sorry,'%s' is not in process list,may be not running......'''%processname
        status = 0
        pid = 0
        time1 = time.ctime()
    return (processname,time1,pid,status)

print getinfo('QQ.exe')

    
