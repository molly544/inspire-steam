import time
import pySimVerse

#Initialize drone and environment,
drone = pySimVerse.Drone()
env = pySimVerse.Environment('garage')

#Set drone properties for minimal flight time,
drone.set_altitude(0.1)  # Low altitude
drone.set_velocity(0.1)  # Minimal velocity

#Start simulation,
start_time = time.time()
drone.takeoff()
while drone.is_flying():
    drone.update()
end_time = time.time()

#print shortest flight time
print("shortest flight time:",end_time-start_time,"seconds")
