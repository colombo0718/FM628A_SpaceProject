from machine import I2C, Pin
import machine
import mpu6050
import time
import network
import socket

spacecraft_name='spacecraft'
spacecraft_code='12345678'
  
i2c = I2C(scl=Pin(5),sda=Pin(4))
accelerometer = mpu6050.accel(i2c)
 
while(accelerometer.get_values()['AcX']==0 and
      accelerometer.get_values()['AcY']==0 and
      accelerometer.get_values()['AcZ']==0):
    pass

ap=network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=spacecraft_name,password=spacecraft_code)

# while True:

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

        six_data = accelerometer.get_values()
           
        data+=str(six_data['AcX'])+','
        data+=str(six_data['AcY'])+','
        data+=str(six_data['AcZ'])+','
        
        data+=str(six_data['GyX'])+','
        data+=str(six_data['GyY'])+','
        data+=str(six_data['GyZ'])+'/'
        

        
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
