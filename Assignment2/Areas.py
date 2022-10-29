
# Calculate area of circle
a = input("Enter radius of circule :")
radius = int(a)
print("Pi = 3.14","\n" "Radius =", radius,"cm")

area = 3.14*radius*radius
print("Area of circle is ", area,"cm")

area_in_mm = area * 10
area_in_meter = area / 100
area_in_feet = area / 30.48

print("Area of circle in mm :", area_in_mm, "mm")
print("Area of circle in meter :", area_in_meter, "m")
print("Area of circle in feet :", area_in_feet, "ft")

# Calculate area of rectangle
a = input("Enter height of rectangle :")
b = input("Enter width of rectangle :")
height = int(a)
width = int(b)
print("Height =", height,"\n" "Width =", width)

area = height*width
print("Area of rectangle is ", area)

area_in_mm = area * 10
area_in_meter = area / 100
area_in_feet = area / 30.48

print("Area of rectangle in mm :", area_in_mm, "mm")
print("Area of rectangle in meter :", area_in_meter, "m")
print("Area of rectangle in feet :", area_in_feet, "ft")


# Calculate area of square
a = input("Enter side length of square :")
side = int(a)
print("Side =", side)

area = side*side
print("Area of square is ", area)

area_in_mm = area * 10
area_in_meter = area / 100
area_in_feet = area / 30.48

print("Area of square in mm :", area_in_mm, "mm")
print("Area of square in meter :", area_in_meter, "m")
print("Area of square in feet :", area_in_feet, "ft")
