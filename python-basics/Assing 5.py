#Maureen Mbugua
#13/02/2026
#programme to calculate income tax

salary =int(input("enter your gross salary"))

if salary<45000:
    tax=(0.05 * salary)/100
    net_salary=salary-tax


print(f"gross salary ={salary}")
print(f"net_salary ={net_salary}")
print(f"tax={tax}")

elif 50000<=salary and salary<100000:
    tax=(0.05*salary)/100
    net_salary=salary-tax

print(f"gross salary ={salary}")
print(f"net_salary ={net_salary}")
print(f"tax={tax}")

elif salary>=100000:
    tax=(7.5*salary)/100
    net_salary=salary-tax
    
print(f"gross salary ={salary}")
print(f"net_salary ={net_salary}")
print(f"tax={tax}")



