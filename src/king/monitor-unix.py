#!/user/bin/env python
#encoding:utf-8

'''
监控linux服务，并返回运行状态  
'''

import paramiko
import time

def server_connect(): 
    #连接unix服务器，判断服务是否启动
    result_list = []    
    for i in range(len(server)):
        processname = server[i][0]
        hostname = server[i][1]
        port = server[i][2]
        username = server[i][3]
        password = server[i][4]
        '''
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)
        
        stdin, stdout, stderr = ssh.exec_command('service %s status'%processname) 
        result = stdout.readlines()
        ssh.close() 
        '''
        
        if processname != 'tomcat':  
            a = '%s running'%processname
        else:
            a = tomcat_connect()
        result_list.append(a)
      
    return ' ; '.join(result_list)
        
def tomcat_connect(): 
    #tomcat服务需要特殊判断  
    return 'tomcat down'

def message(): 
    print  result

if __name__ == '__main__': 
    l0= ['mysql1','192.168.0.82','22','root','stcy@2014']
    l1= ['mysql2','192.168.0.82','22','root','stcy@2014']
    l2= ['mysql3','192.168.0.82','22','root','stcy@2014']
    l3= ['tomcat','192.168.0.82','22','root','stcy@2014']
    server = [l0,l1,l2,l3]
    
    result = server_connect()
    
    if 'down' in result:
        message()
    else:
        print 'OK'

        

