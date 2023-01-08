import math
def area_of_circle():
    pi = 3.14
    r = int(input("Enter your radius:"))
    area = (pi *(pow(r, 2)))
    print(f"The Area of the circle is {area}")
def circumference_of_circle():
    pi = 3.14
    r = int(input("Enter radius:"))
    c = (2*pi*r)
    print( f"The circumference is {c}" )
def area_for_triangle():
    b =int(input("Enter your base:"))
    h =int(input("Enter your height:"))
    area=(1/2)*b*h
    print(f"The Area of the Triangle is {area}")
def perimeter_for_triangle():
    b =int(input("Enter your base:"))
    h =int(input("Enter your height:"))
    perimeter=(a+b+c)
    print(f"The perimeter of the triangle is {perimeter}")   
def area_of_square():
    l =int(input("Enter your length:"))
    
    area=(l**2)
    print(f"The area of a square is {area}")
def perimeter_of_square():
    l =int(input("Enter your length:"))

    perimeter=(4*a)
    print(f"The perimeter of a square is {perimeter}")
def area_of_rectangle():
        l =int(input("Enter your length:"))
        w =int(input("Enter your width:"))
        area=(l*w)
        print(f"The area of a rectangle is {area}")
def perimeter_of_rectangle():
    l =int(input("Enter your length:"))
    w =int(input("Enter your width:"))
    perimeter=(l*w)
    print(f"The perimeter of a rectangle is {perimeter}")
def area_of_Parallelogram():
    b=int(input("Enter your base:"))
    h =int(input("Enter your vertical height:"))
    area=(b*h)
    print(f"The area of a parallelogram is {area}")
def perimeter_of_Parallelogram():
    b=int(input("Enter your base:"))
    h =int(input("Enter your vertical height:"))
    perimeter=( 2(l + w))
    print(f"The perimeter of a parallelogram is {perimeter}")
while True:
    print("""Welcome to Area and Perimeter calculator
            Enter 1 for area of a Circle
            Enter 2 for circumference of a Circle 
            Enter 3 for area of Triangle
            Enter 4 for perimeter of Triangle
            Enter 5 for area of Square
            Enter 6 for perimeter of Square
            Enter 7 for area of Rectangle
            Enter 8 for perimeter of Rectangle
            Enter 9 for area of Parallelogram
            Enter 10 for perimeter of Parallelogram
""")
    option = int(input("Enter your option from above:"))
    if option == 1:
        area_of_circle()
    elif option == 2:
        circumference_of_circle()
    elif option == 3:
        area_for_triangle()
    elif option== 4:
        perimeter_for_triangle()
    elif option == 5:
        area_of_square()
    elif option == 6:
        perimeter_of_square()
    elif option == 7:
        area_of_rectangle()
    elif option == 8:
        perimeter_of_rectangle()
    elif option == 9:
        area_of_Parallelogram()
    elif option == 10:
        perimeter_of_Parallelogram()
    else :
        print("Invalid option")
         
