import socket
import time
import random
import pygame as pg

#設定視窗
pg.init()
width, height = 600, 400                     
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("Lab08 Shoot Rocket")     

#建立畫布bg
bg = pg.Surface(screen.get_size())
bg.fill((255,255,255))
pg.display.update()

#建立圖片物件
spacecraft = pg.image.load("pics/spacecraft.png")
platform = pg.image.load("pics/platform.png")

redfire1 = pg.image.load("pics/redFire1.png")
redfire2 = pg.image.load("pics/redFire2.png")
redfire=[redfire1,redfire2]

greenfire1 = pg.image.load("pics/greenFire1.png")
greenfire2 = pg.image.load("pics/greenFire2.png")
greenfire=[greenfire1,greenfire2]

# 連線太空船
sock=socket.socket()
sock.connect(('192.168.4.1', 9999))    #IP位址需要做更改

y=400-90

i=0
running=True
while running:
    data=sock.recv(1024)
    data=data.decode('utf-8')
    data=data.split('/')

    for i in range(len(data)-1) :
        components=data[i].split(',')

        if len(components)==9 and not components[0]=="":
            print(components)
            
            y-=1

            bg.fill((0,255,255))
            bg.blit(spacecraft,(300-20,y))
            bg.blit(platform,(300-30,400-30))

            bg.blit(redfire[i%2],(300-20,y+60))
            bg.blit(greenfire[i%2],(300-20,y+60))
            screen.blit(bg, (0,0))
            pg.display.update()
            time.sleep(0.005) 

#             bg.blit(redfire[i%2],(300-20,y+60))
#             bg.blit(greenfire[i%2],(300-20,y+60))
#             screen.blit(bg, (0,0))
#             pg.display.update()
#             time.sleep(0.005)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit() 
sock.close()       

