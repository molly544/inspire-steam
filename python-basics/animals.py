#Maureen Mbugua
#23/02/2026
#programme to show inheritance in python


class Animal():
    def __init__(self,colour,weight,food):
        self.species = species
        self.weight = weight
        self.food = food
        

    def self(self,weight):
        
        print(f"the animal weighs {weight}")
    
    
    def eat(self,food):
        print("the animal eats {food}")


class Dog():
    def __init__(self,species,weight,food):
        super().__init__(species,weight,food)
        self.colour= colour
        self.breed = breed
        self.weight = weight
        self.foof = food
    def grow(self,weight):
        weight=1.1*weight
        print(f"the animal weighs {weight}")
    
    def eat(self,food):
        print("the animal eats {food}")
    def barks(self,):
        print("the dog says woof woof")

class Horse():
    def __init__(self,species,weight,food):
        self.colour = colour
        self.breed = breed
        self.weight = weight
        self.food = food
    def grow(self,weight):
        weight=1.1*weight
        print(f"the animal weighs {weight}")
    
    
    def eat(self,food):
        print("the animal eats {food}")

