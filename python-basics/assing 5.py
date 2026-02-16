#Maureen Mbugua
#13/02/2026
#programme to calculate income tax

salary =int(input("enter your gross salary"))

if salary<45000:
    tax=(5%*salary)/100
    net_salary=salary-tax
    
