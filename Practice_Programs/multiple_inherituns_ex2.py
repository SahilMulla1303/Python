class cal():
    def __init__(self):
        self.a = 30
        self.b = 10
    def add(self):
        c = self.a + self.b
        print(c)

class cal2():
    def __init__(self):
        self.y = 50
        self.z = 4
    def add1(self):
        d = self.y + self.z
        print(d)
class cal3(cal,cal2):
    def __init__(self):
        self.p = 100
        self.q = 200
        cal.__init__(self)
        cal2.__init__(self)
    def power(self):
        print(self.b**self.z)


o3 = cal3()
o3.power()