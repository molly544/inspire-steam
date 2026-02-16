#Maureen Mbugua
#16/02/2026
#program to calculate factorials of a number

number=int(input("enter the number x:"))
factorial=1# initialise factorial as 1
for x in range(1,number+1):
    factorial *=x
    number=number-1 

print(f"{number}!={factorial}")