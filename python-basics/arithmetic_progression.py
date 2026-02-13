#Maureen Mbugua
#13/02/2026
#programme to calculate arithmetic progression

#calculating the nth number

a=int(input("enter the first number:"))
n=int(input("enter the number of terms:"))
d=int(input("enter common difference:"))

nth_term=a+(n-1)*d
Sn=(n/2)*((2*a) + (n-1)*d)

print(F"the nth term is:{nth_term}")
print(f"the Sn is:{Sn}")
