import time
from machine import I2C, Pin
from mpu9250 import MPU9250

i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
#     print("Ax:",sensor.acceleration[0],",Ay:",sensor.acceleration[1],",Ay:",sensor.acceleration[2])
    print("Gx:",sensor.gyro[0],",Gy:",sensor.gyro[1],",Gz:",sensor.gyro[2])
#     print("Bx:",sensor.magnetic[0],",By:",sensor.magnetic[1],",Bz:",sensor.magnetic[2])
#     print(sensor.temperature)

    time.sleep(.1)