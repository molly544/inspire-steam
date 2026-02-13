#Maureen Mbugua
#13/02/2026
#programme to calculate geometric progression

#calculating the nth number

a=float(input("enter the first number:"))
r=float(input("enter the common ratio:"))
n=int(input("enter the numberof terms:"))

nth_term=a*(r**(n-1))
Sn=a*(1-r**n)/(1-r)

print(F"the nth term is:{nth_term}")
print(f"the Sn is:{Sn}")
