#Maureen Mbugua
#17/02/2026
#programme to preform arithemetic operations

f_number=12#first number
s_number=18#second number

sum_number=f_number+s_number 
difference_numbers=f_number-s_number
quotient_numbers=f_number/s_number
product_numbers=f_number*s_number


print("sum of the numbers%d"%sum_number)
print("quotient of the numbers %0.2f"%quotient_numbers)

#modulos-remaider
print(4%5)

#even and odd numbers
for x in range(0,16):
    if (x%2==1):
        print("{x} is odd number")
    elif(x%2==0):
        print("{x}is even number")
    print(x)
