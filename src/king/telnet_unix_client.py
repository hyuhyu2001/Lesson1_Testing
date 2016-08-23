#!/user/bin/env python
#encoding:utf-8

'''
模拟telnet客户端的操作
通过CMD执行一段命令，自动执行unix服务器上的命令，并将结果返回
在cmd中可以通过运行python脚本就可以执行
'''
import telnetlib

def telnetdo(HOST,PORT,user,password,finish,command):
    tn=telnetlib.Telnet(HOST,PORT,timeout=10)#telnet 默认是23端口，telnet时必须打开,服务端已改为8020
    tn.set_debuglevel(2)# 设置debug级别
    
    #输入登录用户名 
    tn.read_until('login: ')
    tn.write(user + '\n')
    
    #输入登录密码
    tn.read_until('Password: ')
    tn.write(password + '\n')
    
    # 登录完毕后，执行命令
    tn.read_until(finish)  
    for i in range(len(command)):
        tn.write(command[i] + '\n')
        tn.read_until(finish)  
    
    result = tn.read_very_eager()  
    print result
    
    # 命令执行完毕后，终止Telnet连接（或输入exit退出）
    tn.close()

if __name__ =='__main__':
    HOST = '192.168.7.82' #telnet服务器IP
    PORT='8020'
    user = 'jinzj' #登陆用户名
    password = 'Yy@19811008' #登陆密码
    finish = '[jinzj@localhost ~]$'      # 命令提示符（标识着上一条命令已执行完毕） 
    command = ['pwd','ls']
    telnetdo(HOST,PORT,user,password,finish,command)