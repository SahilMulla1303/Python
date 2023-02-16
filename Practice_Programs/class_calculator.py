class calculator():
    def __int__(self):
        self.a = 7
        self.b = 5
    def add(self):
        c=self.a+self.b
        print(c)
    def sub(self):
        c=self.a-self.b
        print(c)
    def mul(self):
        c=self.a*self.b
        print(c)
    def power(self):
        c=self.a**self.b
        print(c)

obj = calculator()
obj.__int__()
obj.add()
