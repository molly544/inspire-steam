#Maureen Mbugua
#23/02/2026
#programme to show classes in python

class Car():
    # attributes of the car
    def __init__(self,model,make,colour,year):
        self.model=model
        self.make=make
        self.colour=colour
        self.year=year
    # print car details
    def print_details(self,model,make,colour,year):
        print(f"{make} {model} of colour {colour} was manufactured in the year {year}")

    #instantiate a class object

    my_car = Car("audi","u8","white","2025")
    dads_car = Car("toyota","jeep","black","2025")

    my_car.print_details("audi","u8","white","2025")
    

    

