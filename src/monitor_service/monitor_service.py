#!/user/bin/env python
#encoding:utf-8

'''
监控线上服务器的服务，在服务出现停止的时候发短信
'''
import time
import sys

#简单的monitor函数，主要监控一个远程服务是否还在,system 是一个系统model
def monitor(system):
    last_monitor_status=True
    TimeInterval=10
    while True:
        is_active = check_system_status(system.env.env_ip,system.env.env_port,system.env.get_env_path())
        if is_active==False and last_monitor_status==True:
            '''
            system is down,do something
            '''
            pass

        elif is_active==True and last_monitor_status==False:
            '''
            system revover
            '''
            pass
        else:
            pass
        last_monitor_status=is_active
        time.sleep(TimeInterval)


if __name__=="__main__":
    system=sys.argv[1]
    monitor(system)
    