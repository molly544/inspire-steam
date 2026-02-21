#Maureen Mbugua
#19/02/2026
#programme to show objects

class Human:
    #first we define attributes of human beings
    type="Mammal"
    legs=2
    brain=True
    warm_blooded=True 

    #we then create a constructor for the class object
    #the constructor will be used to create copies of this object
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def tell_story(self):
        print(f"Hello,i am {self.name} here is a story")
        print(f"There were hares everywhere in the past")


Rose=Human("Rose",19)
Lexie=Human("Lexie",20)

#Let humans created do things
Rose.tell_story()
print(f"Rose's age is:",Rose.age)

#modify one of the objects,without modifying other objects
Lexie.city="Mombasa"
Rose.city="Malindi"

print(f"Lexie's location:",Lexie.city)
print(f"Rose's location:",Rose.city)

        