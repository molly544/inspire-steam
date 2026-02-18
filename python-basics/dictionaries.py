#Maureen Mbugua
#18/02/2026
#programme to show use of dictionaries in python

cars={"model":"audi" ,"make":"u8" ,"colour":"white" ,"year":2025}

print(cars)
print(cars["year"])
print(cars["model"])
print(cars["make"])

students=dict("Alice": 24,
              "Alex": 19,   
              "Jace": 22,
              "Jake": 23)

for key in students:
    print(key)

for val in students.values():
    print(val)