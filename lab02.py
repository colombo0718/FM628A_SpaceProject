import socket
import time
import pygame as pg

pg.init()

#設定視窗
width, height = 640, 480                      
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("Shoot Rocket")         
#建立畫布bg
bg = pg.Surface(screen.get_size())

# screen=pg.transform.rotozoom(screen,1,2)

bg.fill((0,255,255))
pg.display.update()

spacecraft = pg.image.load("pics/spacecraft.png")
spacecraft = pg.transform.scale(spacecraft, (82,120))
# spacecraft = pg.transform.rotate(spacecraft,45)

bluefire1 = pg.image.load("pics/blueFire1.png")
bluefire1 = pg.transform.scale(bluefire1, (82,60))
bluefire2 = pg.image.load("pics/blueFire2.png")
bluefire2 = pg.transform.scale(bluefire2, (82,60))
bluefire=[bluefire1,bluefire2]



# bg.blit(spacecraft,(0-40,0))
# bg.blit(bluefire[1],(0-40,0+120))
screen.blit(bg,(0,0))
pg.display.update()


sock=socket.socket()
sock.connect(('192.168.4.1', 9999))    #IP位址需要做更改

i=0

cnt=0

running=True
while running:
    data=sock.recv(1024)
    data=data.decode('utf-8')
    data=data.split('/')
    print(data)
    for i in range(len(data)-1) :
        components=data[i].split(',')

        # if len(components)==6 and not components[0]=="":
        cnt+=1
        cnt=cnt%2

        bg.fill((0,255,255))

        bg.blit(spacecraft,(320-40,240))
        bg.blit(bluefire[cnt],(320-40,240+120))
        
        screen.blit(bg,(0,0))
        pg.display.update()

        time.sleep(0.01)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
pg.quit() 
sock.close()            #關閉 socket        

