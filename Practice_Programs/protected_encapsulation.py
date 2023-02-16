class cal:
    def __init__(self,a,b):
        self._a = a
        self.b = b
        self._s = 500
    def add(self):
        c = self._a + self.b
        return c

class num():
    def __init__(self):
        self.x = 100
        self.y = 50
    def sum(self):
        print(self.x + self.y + self._a) #self._a is a protected variable

obj1 = cal(20,10)
obj2 = num()
print(obj1.add())
obj2.sum()
print(obj1._s)