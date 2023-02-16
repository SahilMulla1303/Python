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

# o1 = cal()
o2 = cal2()
o2.add1()