from areas_module import *

while True:
    print("Calculate Areas : \n 1.Circle \n 2.Rectangle \n 3.Square")
    c=int(input("Enter no of which area want to calculate :"))

    if(c==1):
        pi = 3.14
        radius = int(input("Enter radius of circle :"))
        print("Pi =", pi,"\n" "Radius =", radius)
        print("Area of circle is ", circle(pi,radius))
    elif(c==2):
        height = int(input("Enter height of rectangle :"))
        width = int(input("Enter width of rectangle :"))
        print("Height =", height,"\n" "Width =", width)
        print("Area of rectangle is ", rectangle(height,width))
    elif(c==3):
        side = int(input("Enter side of square:"))
        print("Side =", side)
        print("Area of square is ", square(side))

    b=input("You want to more num_sum(y/n):")
    print()
    if b=="n":
        print("******************************************")
        print("Thank you")
        break
