class marks:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        # print(self.a + self.b)
    def __add__(self,other):
        x = self.a + other.a
        y = self.b + other.b
        z = marks(x,y)
        return z

m1 = marks(50,60)
m2 = marks(70,75)
m3 = m1 + m2
print(m3.a + m3.b)

# this methods are magical methods

# a = 20
# b = 30
# # print(a+b) > gt  >= ge
# print(int.__add__(a,b))
# print(int.__sub__(100,40))