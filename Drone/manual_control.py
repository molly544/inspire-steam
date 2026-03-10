from pysimverse import Drone
import time
import cv2

drone = Drone()
drone.connect()
time.sleep(2)

drone.take_off(6)
rc_speed=200

while True:
    Key = cv2.waitKey(1)&0xff

    #get all values to zero 
    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    if Key==ord("w"):
        forward_backward=rc_speed

    elif Key==ord("s"):
        
        forward_backward = rc_speed

    elif Key==ord("a"):
        left_right = rc_speed 

    elif Key==ord("d"):
        left_right = rc_speed

    
    elif Key==ord("f"):
        up_down = rc_speed 

    elif Key==ord("c"):
        up_down = rc_speed 

    elif Key==ord("e"):
        yaw = 1

    elif Key==ord("e"):
        yaw = 1

    elif Key==ord("1") or Key==27:
        drone.land()
        time.sleep(2)
        break

    drone.send_rc_control(left_right,forward_backward,up_down,yaw)