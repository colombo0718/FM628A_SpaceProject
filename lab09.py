import socket
import time
import random
import pygame as pg

#設定視窗
pg.init()
width, height = 600, 400                     
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("Lab09 Shoot Rocket")     

#建立畫布bg
bg = pg.Surface(screen.get_size())
bg.fill((255,255,255))
pg.display.update()

#建立圖片物件
spacecraft = pg.image.load("pics/spacecraft.png")

redfire1 = pg.image.load("pics/redFire1.png")
redfire2 = pg.image.load("pics/redFire2.png")
redfire=[redfire1,redfire2]

greenfire1 = pg.image.load("pics/greenFire1.png")
greenfire2 = pg.image.load("pics/greenFire2.png")
greenfire=[greenfire1,greenfire2]

cloud1 = pg.image.load("pics/cloud1.png")
cloud2 = pg.image.load("pics/cloud2.png")
cloud3 = pg.image.load("pics/cloud1.png")


class stickers():

    def __init__(self,source,background):
        self.i=0
        self.x=0
        self.y=0
        self.image=pg.image.load(source)
        self.background=background

    def stickOn(self,background,position):
        self.x=position[0]
        self.y=position[1]
        background.blit(self.image,position)

    def move(self,background,displace=False):
        self.x+=displace[0]
        self.y+=displace[1]
        background.blit(self.image,(self.x,self.y))
    

cloud1= stickers("pics/cloud1.png",bg)
cloud2= stickers("pics/cloud2.png",bg)
cloud3= stickers("pics/cloud1.png",bg)

thunder = stickers("pics/thunder.png",bg)

satellite = stickers("pics/satellite.png",bg)

cloud1.stickOn(bg,(200,200))
cloud2.stickOn(bg,(400,150))
cloud3.stickOn(bg,(300,100))

thunder.stickOn(bg,(100,300))

satellite.stickOn(bg,(0,300))

screen.blit(bg, (0,0))
pg.display.update()

# 連線太空船
sock=socket.socket()
sock.connect(('192.168.4.1', 9999))    #IP位址需要做更改

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

            bg.fill((0,255,255))
            

            cloud1.move(bg,(0,1))
            cloud2.move(bg,(0,1))
            cloud3.move(bg,(0,1))
            thunder.move(bg,(0,1))

            satellite.move(bg,(5,0))

            bg.blit(spacecraft,(300-20,200)) 
            
            if cloud1.y>400 :
                cloud1.x=random.randint(0,600)
                cloud1.y=-100
            if cloud2.y>400 :
                cloud2.x=random.randint(0,600)
                cloud2.y=-100
            if cloud3.y>400 :
                cloud3.x=random.randint(0,600)
                cloud3.y=-100
            if thunder.y>400 :
                thunder.x=random.randint(0,600)
                thunder.y=-100
            if satellite.x>600 :
                satellite.x=-100
                satellite.y=random.randint(0,400)

            bg.blit(redfire[0],(300-20,200+60))
            bg.blit(greenfire[0],(300-20,200+60))
            screen.blit(bg, (0,0))
            pg.display.update()
            time.sleep(0.005) 

            bg.blit(redfire[1],(300-20,200+60))
            bg.blit(greenfire[1],(300-20,200+60))
            screen.blit(bg, (0,0))
            pg.display.update()
            time.sleep(0.005)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit() 
sock.close()       

