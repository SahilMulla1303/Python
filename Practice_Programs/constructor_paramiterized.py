class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a,self.b)
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

obj = calculator(15,10)
obj.add()
