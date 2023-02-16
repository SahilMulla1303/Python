class demo1:
    def method1(self):
        print("This is method 1 from class demo 1")

class demo2():
    def method2(self):
        print("This is method 2 from class demo 2")

class demo3(demo1,demo2):
    def method3(self):
        print("This is method 3 from class demo 3")

o = demo3()
o.method1()
o.method2()
o.method3()