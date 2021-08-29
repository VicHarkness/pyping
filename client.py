#!/usr/bin/env python3

import socket
from datetime import datetime
import codecs
import time

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

for x in range(100):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        #while True:
       # currentTime=datetime.now()
        dateTimeObj = datetime.now()
        microsec = dateTimeObj.microsecond
        sec=dateTimeObj.second
        #print(microsec)
        #test=(timeObj).to_bytes(4, byteorder='big')
        microsecStr=str(microsec)
        msleng=len(microsecStr)
        if msleng!=6:
            microsecStr2=("0"*(6-msleng))+microsecStr
        else:
            microsecStr2=microsecStr
        secStr=str(sec)
        xStr=str(x)
        microsecEnc=codecs.encode(microsecStr2,'UTF-8')
        secEnc=codecs.encode(secStr,'UTF-8')
        xEnc=codecs.encode(xStr,'UTF-8')
        print(xEnc,sec,microsecStr2)
        s.sendall(xEnc+b' '+secEnc+microsecEnc)
        time.sleep(1)
        #data = s.recv(1024)
        s.close()

#print('Received', repr(data))
