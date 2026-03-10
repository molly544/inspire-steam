#Maureen Mbugua
#09/03/2026

from pysimverse import Drone
import time

#create an instance of drone
drone = Drone()
drone.connect()
drone.take_off()
#distance in cm

drone.move_forward(280)
drone.move_backward(370)
drone.move_right(80)
drone.move_left(80)

time.sleep(2)

drone.land()