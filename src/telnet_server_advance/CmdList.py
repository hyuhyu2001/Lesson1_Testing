#!/user/bin/env python
#encoding:utf-8

import os
import win_server as w

CommandList = {'ls':'tasklist','ll':'QQ.exe'}

def get_cmd_status(conn,newline):
    while True:
        name = 'enter your command:'
        w.send_result(conn,name)
        data = w.parse_input(conn,newline)
        if data in CommandList.keys():
            name = get_cmd_result(conn,newline,data)
            w.send_result(conn,name)
            continue
        elif data == 'exit':
            w.quit_status(conn)  #调用退出函数
            break
        else:
            name = 'command is Wrong'+newline
            w.send_result(conn,name)
            continue
    
def get_cmd_result(conn,newline,data):
    task = os.popen(CommandList[data])
    if CommandList[data] in task.read():
        name = 'perfect'+newline
    else:
        name = 'so bad'+newline
    return name

