#!/user/bin/env python
#encoding:utf-8

import os
from win_server import *
from telnet_public import *

CommandList = {'ls':'tasklist','ll':'QQ.exe'}

def get_cmd_status(status,conn,newline):
    while True:
        name = 'enter your command:'
        send_result(status,conn,name)
        data = parse_input(conn,newline)
        if data in CommandList.keys():
            name = get_cmd_result(conn,newline,data)
            send_result(status,conn,name)
            continue
        elif data == 'exit':
            quit_status(conn)  #调用退出函数
            break
        else:
            name = 'command is Wrong'+newline
            send_result(status,conn,name)
            continue
    
def get_cmd_result(conn,newline,data):
    task = os.popen(CommandList[data])
    if CommandList[data] in task.read():
        name = 'perfect'+newline
    else:
        name = 'so bad'+newline
    return name

