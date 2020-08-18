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
print(ap.ifconfig())

sock=socket.socket() # 建立socket 
sock.bind(('0.0.0.0',9999)) # ip+port,0.0.0.0表示所有ip皆可以接收
sock.listen(1) # 只允許一個連接

(csock, adr) = sock.accept()
print('connect success',)

n=0
while True:
    n+=1
    print(n)
    get=csock.recv(1024)
    get=get.decode('utf-8')
    print("get:",get)
    put='this is '+spacecraft_name
    put=put.encode('utf-8')
    csock.send(put)
    print('put:',put)
    
    time.sleep(.1)