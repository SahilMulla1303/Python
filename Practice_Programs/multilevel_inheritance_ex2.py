class cal():
    def __init__(self):
        self.a = 30
        self.b = 10
    def add(self):
        c = self.a + self.b
        print(c)

class cal2(cal):
    def __init__(self):
        self.y = 50
        self.z = 40
        cal.__init__(self)
    def add1(self):
        d = self.y + self.z + self.a
        print(d)
class cal3(cal2):
    def __init__(self):
        self.p = 100
        self.q = 200
        cal2.__init__(self)
    def power(self):
        print(self.b**self.z)


# o1 = cal()
o3 = cal3()
o3.power()