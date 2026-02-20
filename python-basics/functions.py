#Maureen Mbugua
#19/02/2026
#programme to display functions

def cook_egg():
    oil="20ml"
    pan=True
    fire=True
    eggs="3"

    print(f"the pan is{pan},the fire is{fire},/add{oil} and cook{eggs}eggs")

print("here is statement 1")

print("here is statement 2")

cook_egg()
print("here is statement 3")

#bolt fares creating functions
def  creating_fares(route,distance,is_rush_hour):
    fare=distance*15
    if is_rush_hour==True:
        fare=(distance*15)*2
    print(f"our fare to {route} is {fare}")
     

rush_hour=True 
Returned_fare=creating_fares("Juja-Kimbo",10,rush_hour) 
print(f"the fare is returned:",Returned_fare) 
creating_fares("Juja-Kimbo",10,rush_hour)


#passing a list as a parameter
def writing_all_interests(interests):
    for interests in interests:
        print(f"I am interested in {interests}")

all_interests=["writing books","poetry","law","sleeping"]

writing_all_interests(all_interests)








