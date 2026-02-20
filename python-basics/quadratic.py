#Maureen Mbugua
#17/02/2026
#programme to solve quadratic equations

import math

def solve_quadratic(a,b,c):
    """solve a quadratic equation of theform ax^2+bx+c=0"""
    discriminant=b**2-4*a*c

    if discriminant>0:
        root1=(-b+math.sqrt(discriminant))/(2*a)
        root2=(-b-math.sqrt(discriminant))/(2*a)
        return f"two distinct roots:{root1}and{root2}"

    elif discriminant==0:
        root=-b/2*a
        return f"one repeated root:{root}"

    else:
        real_part=-b/(2*a)
        imaginary_part=math.sqrt(-discriminant)/2*a
        return f"two complex roots:{real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i"


def main():
    a=float(input("enter coefficient a:"))
    b=float(input("enter coefficient b:"))
    c=float(input("enter coefficient c:"))

    print(solve_quadratic(a,b,c))

if __name__=="__main__":
    main()
     


