from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off(100)

drone.move_forward(100)
drone.move_right(300)

drone.land