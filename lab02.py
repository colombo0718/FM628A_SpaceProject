import time
from machine import ADC, Pin
adc = ADC(0)

while True:
    print(adc.read())
    time.sleep(.05)