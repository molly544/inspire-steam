#Maureen Mbugua
#17/02/2026
#programme to display a diamond using*and triangle

def print_triangle(n):
    """print a triangle of asterisks"""
    for i in range(n):
        print(''*(n-i-1)+'*'*(2*i+1))

def print_diamond(n):
    """print a diamond of asterisks"""
    #print top half of diamond
    for i in range(n):
        print(''*(n-i-1)+'*'*(2*i+1))
    #print bottom half of diamond
    for i in range(n-2,-1,-1):
        print(''*(n-i-1)+'*'*(2*i+1))

def main():
    n=int(input("enter the size of the triangle/diamond"))
    print("triangle:")
    print_triangle(n)
    print("\nDiamond:")
    print_diamond(n)

if __name__ == "__main__":
    main()


