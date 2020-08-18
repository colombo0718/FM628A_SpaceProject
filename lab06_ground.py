import socket
import time

sock=socket.socket()
sock.connect(('192.168.4.1', 9999))    #IP位址需要做更改

n=0
while True:
    n+=1
    print(n)
    put='call spacecraft'
    put=put.encode('utf-8')
    sock.send(put)
    print('put:',put)
    get=sock.recv(1024)
    get=get.decode('utf-8')
    print("get:",get)

sock.close()

    

