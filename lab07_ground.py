import socket
import time

sock=socket.socket()
sock.connect(('192.168.4.1', 9999))    #IP位址需要做更改
n=0
running=True
while running:
    n+=1

    data=sock.recv(1024)
    data=data.decode('utf-8')
    data=data.split('/')

    for i in range(len(data)-1) :
        components=data[i].split(',')
        if len(components)==9 and not components[0]=="":
            print(components)

sock.close()


    

