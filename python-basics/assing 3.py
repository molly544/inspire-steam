#Maureen Mbugua
#16/02/2026
#program to show for loops in python
import math
from tabulate import tabulate

angles=(0,30,45,60,90)
data[]
for angle in angles:
    rad=math.radians(angle)
    data.append([angle,round(math.sin(rad),4),round(math.cos(rad),4),round(math.tan(rad),4)])

print(f(tabulate{data,headers=['angle','sin','cos','tan'],tablefmt='grid'}))
