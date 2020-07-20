import socket
import time

sock=socket.socket()
sock.connect(('192.168.4.1', 9999))    #IP位址需要做更改
i=0
running=True
while running:
    i+=1
    # sock.send('ready'.encode('utf-8'))
    data=sock.recv(1024)
    data=data.decode('utf-8')
    print(i,data)

    if i>10:
        running=False
sock.close()
#     data=data.split('/')
# #     print(len(data))
#     print(data)
#     for i in range(len(data)-1) :
#         components=data[i].split(',')

#         if len(components)==6 and not components[0]=="":
#             cnt+=1
#             cnt=cnt%2

#             bg.fill((0,255,255))
#             print(components)
#             print(ax,ay,az)
#             ax=abs(float(components[0]))
#             ay=abs(float(components[1])) 
#             az=abs(float(components[2]))

    

