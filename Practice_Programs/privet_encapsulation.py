class cal:
    def __init__(self,a,b):
        self.__a = a
        self.b = b
        self._s = 500
    def add(self):
        c = self.__a + self.b
        return c

class num(cal):
    def __init__(self):
        self.x = 100
        self.y = 50
        cal.__init__(self,3,4)
    def sum(self):
        print(self.x + self.y + self.__a) #self.__a is a privet variable

obj1 = cal(20,10)
obj2 = num()
print(obj1.add())
obj2.sum()
print(obj1.__a)