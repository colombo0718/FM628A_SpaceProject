from machine import I2C, Pin
import machine
from mpu9250 import MPU9250
import time
import network
import socket

spacecraft_name='spacecraft'
spacecraft_code='12345678'

i2c = I2C(scl=Pin(5),sda=Pin(4))
sensor = MPU9250(i2c)

ap=network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=spacecraft_name,password=spacecraft_code)

sock=socket.socket() # 建立socket 
sock.bind(('0.0.0.0',9999)) # ip+port,0.0.0.0表示所有ip皆可以接收
sock.listen(1) # 只允許一個連接


while True:
    
    print("這裡是",spacecraft_name)
    print("等待地面接收站連線")
    (csock, adr) = sock.accept()
    print(adr)
    print("與地面接收站達成連線")
    connect=True
    get='ready'
    i=0 
    while connect:
        i+=1
        
        data='' # 重製data

#     print("Ax:",sensor.acceleration[0],",Ay:",sensor.acceleration[1],",Ay:",sensor.acceleration[2])
#     print("Gx:",sensor.gyro[0],",Gy:",sensor.gyro[1],",Gz:",sensor.gyro[2])
#     print("Bx:",sensor.magnetic[0],",By:",sensor.magnetic[1],",Bz:",sensor.magnetic[2])
        acc=sensor.acceleration
        gyr=sensor.gyro
        mag=sensor.magnetic
        
        data+=str(acc[0])+','+str(acc[1])+','+str(acc[2])+','+str(gyr[0])+','+str(gyr[1])+','+str(gyr[2])+','+str(mag[0])+','+str(mag[1])+','+str(mag[2])+'/'
        
        try:
            n=csock.send(data)     #發出[方向]訊號
            print(n,data)
            print(i,"通訊良好")
        except OSError :
            print("與地面接收站失去連線")
            print('......')
            connect=False
            
        if n<20 :
            print("與地面接收站失去連線")
            print('......')
            connect=False
            
        time.sleep(0.01) # 稍微暫停一下
        
#     sock.close()            #關閉socket