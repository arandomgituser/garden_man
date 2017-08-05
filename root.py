import Switchable
from time import sleep

led = Switchable(5)
while(true):
    led.on()
    sleep(1)
    led.off()
    sleep(1)
