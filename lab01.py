import time
from machine import ADC, Pin
engine = Pin(16,Pin.OUT)
engine.value(0)

while True:
    engine.value(0)
    time.sleep(.1)
    engine.value(1)
    time.sleep(.1)