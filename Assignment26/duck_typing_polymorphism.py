class circle():
    def area(self):
        r = int(input("Enter radius of circle :"))
        area = 3.14 * r * r
        return area

class square():
    def area(self):
        a = int(input("Enter a side of square :"))
        area = a * a
        return area

class Rectangle():
    def area(self):
        w = int(input("Enter width of rectangle :"))
        h = int(input("Enter height of rectangle :"))
        area = w * h
        return area

class area():
    def shapes(self, a):
        b = a.area()
        return b

a = area()

s = square()
r = Rectangle()
c = circle()

b = a.shapes(r)
print(b)

