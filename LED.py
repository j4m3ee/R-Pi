from gpiozero import LED
from time import sleep

led = [LED(26)
,LED(19),LED(13)]

while True:

    for i in range(0,3):
        for j in range(0,3):
            led[j].on()
        led[i].off()
        sleep(1)
            
