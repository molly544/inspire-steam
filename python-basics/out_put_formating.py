#Maureen Mbugua
#17/02/2026
#programme to show different ways of formating 

name="Maureen Mbugua"

weight=62 #weight in kg
fav_team="man_u"

height=125 #weight in centimetres

#1. format using printf("f{}")

print(f"my name is {name} and i weigh {weight}kgs")

#using f_string

msg=f"my name is {name} and i support {fav_team}"

print(msg)

#using {} and . format()

print("my name {0} and i am {1} cms tall".format(name ,height))

#using output specifiers%s - string
import math

print("i support %s"%fav_team)
