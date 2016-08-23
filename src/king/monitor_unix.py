#!/user/bin/env python
#encoding:utf-8

'''
监控linux服务，并返回运行状态，发送短信，此段脚本有以下没实现
（1）没有判断tomcat僵死
（2）响应超过多少秒时，也需要发送预警短信
（3）ssh登陆只通过密码，秘钥的形式不支持
（4）同一服务有多个进程的情况下，比如nginx有多个进程
（5）nginx服务同时存在多个服务器中
（6）ssh登陆只通过密码，秘钥的形式不支持
（7）接口协议只支持http协议，如果是TCP等协议的话如何处理
（8）测试数据、配置和代码分离
'''

import paramiko
import requests

def server_connect(): 
    #连接unix服务器，判断服务是否启动，目前支持用密码登陆，用秘钥登陆的话还需要额外实现
    result_list = []    
    for i in range(len(server)):
        processname = server[i][0]
        hostname = server[i][1]
        port = int(server[i][2])
        username = server[i][3]
        password = server[i][4]
        
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)
       
        if processname != 'tomcat':  
            stdin, stdout, stderr = ssh.exec_command('service %s status'%processname) 
            result = stdout.readlines()
            a = '%s %s'%(processname,result)
            if 'running' in a:
                a = '%s running'%processname
            else:
                a = '%s down'%processname
        else:
            a = tomcat_connect(ssh)
        result_list.append(a)
      
        ssh.close() 
    return ' ; '.join(result_list)
        
def tomcat_connect(ssh): 
    #这段代码只能搞定没有注册服务的情况，但不能搞定tomcat僵死的情况
    stdin, stdout, stderr = ssh.exec_command('ps -ef|grep tomcat|grep -v grep|wc -l') 
    result = stdout.readlines()
    if result == '0': 
        return 'tomcat down'
    else:
        return 'tomcat running'

def message(): 
    #目前接口不能实现自定义模板上传，并发送短信，通过短信验证码实现
    print result
    '''
    for i in range(len(mobile_list)):
        payload = {'mobile': mobile_list[i],'position':'activity-signup'}
        r = requests.get('http://api.00bang.net/sendSmsCode/', params=payload)
        r.url
    '''
if __name__ == '__main__': 
    l0= ['mysql','192.168.7.82','22','root','stcy@2014']
    l1= ['nagios','192.168.7.82','22','root','stcy@2014']
    l2= ['rdisc','192.168.7.82','22','root','stcy@2014']
    l3= ['tomcat','192.168.7.82','22','root','stcy@2014']
    server = [l0,l1,l2,l3]
    
    mobile_list = ['1520000000','15800000000']
    result = server_connect()
    
    if 'down' in result:
        message()
    else:
        print 'OK'