class demo1():
    def method1(self):
        print("This is method 1")
    def method2(self):
        print("This is method 2")

class demo2(demo1):
    def method3(self):
        print("This is method 3")
    def method4(self):
        print("This is method 4")

d1 = demo1()
d1.method1()
d2 = demo2()
d2.method2()
