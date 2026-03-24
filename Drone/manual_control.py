from pysimverse import Drone
import time
import cv2
import keyboard

drone = Drone()
drone.connect()
time.sleep(2)

drone.take_off(6)
rc_speed=200

while True:
    Key = keyboard.read_key()

    #get all values to zero 
    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    if key=="w":
        forward_backward=rc_speed

    elif key=="s":
        
        forward_backward = rc_speed

    elif key=="a":
        left_right = rc_speed 

    elif key=="d":
        left_right = rc_speed

    
    elif key=="f":
        up_down = rc_speed 

    elif Key=="c":
        up_down = rc_speed 

    elif key=="e":
        yaw = 1

    elif key=="e":
        yaw = 1

    elif key=="1" or Key==27:
        drone.land()
        time.sleep(2)
        break

    drone.send_rc_control(left_right,forward_backward,up_down,yaw)