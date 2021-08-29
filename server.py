#!/usr/bin/env python3

import socket
from datetime import datetime
import codecs

print('time:', datetime.now())

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            diff=0
            diffms=0
            #print('Connected by', addr)
            dateTimeObj=datetime.now()
            microsec=dateTimeObj.microsecond
            sec=dateTimeObj.second
            sec2=sec*1000000
            localms=sec2+microsec
            #print(sec2, microsec)
            print(localms)
            data = conn.recv(2048)
            dedata=codecs.decode(data,'UTF-8')
            splitdata=dedata.split()
            dedata2=int(splitdata[1])
            diff=localms-dedata2
            diffms=(diff)/1000
            #print(diff)
            #print(dedata)
            #print('time:', datetime.now())
            
            print("Message %s received from %s with difference: %s ms"%(splitdata[0],addr,diffms))
            #if not data:
             #   break
            conn.sendall(data)
            conn.close()
