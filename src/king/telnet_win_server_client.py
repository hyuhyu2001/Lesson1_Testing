#!/user/bin/env python
#encoding:utf-8

import socket

host = '127.0.0.1'
port = 126
sk= socket.socket()
sk.connect((host,port))
sk.settimeout(5)

while True:
    data = sk.recv(1024)
    print data
    inp = raw_input('please input:')
    sk.sendall(inp)
    if inp == 'exit':
        break

sk.close()