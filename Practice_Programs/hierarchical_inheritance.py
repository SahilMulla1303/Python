class demo1:
    def method1(self):
        print("This is method 1 from class demo 1")

class demo2(demo1):
    def method2(self):
        print("This is method 2 from class demo 2")

class demo3(demo1):
    def method3(self):
        print("This is method 3 from class demo 3")

o = demo2()
o1 = demo3()
o.method1()

o1.method1()