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

max_duration = 5  # safety limit (seconds)

while drone.is_flying():
    drone.update()
#Stop after max_duration to avoid infinite loop,
    if time.time() - start_time > max_duration:
        drone.land()
        break

end_time = time.time()

#Calculate total flight time,
flight_time = end_time - start_time
print(f"Flight Time: {flight_time:.2f} seconds")