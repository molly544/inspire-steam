#Maureen Mbugua
#26/02/2026
#programme to blink leds
from machine import Pin
import time
import machine

red_led = Pin(28, Pin.OUT)
yellow_led = Pin(27, Pin.OUT)
#button input
green_button = Pin(22, Pin.IN,PIN.PULL.UP)
while  True: 
    button_status =  green_button.value()
    red_led.on()
    yellow_led.off()
    time.sleep(1) # Wait for USB to become ready
    red_led.off()
    yellow_led.on()
    time.sleep(1)
    print("learning iot")


