class demo1():
    def test1(self):
        print("this is test1 method from demo1")
class demo2(demo1):
    def test2(self):
        print("this is test2 method from demo2")
    def test1(self):
        print("this is test1 method from demo2")

obj1 = demo2()
obj1.test1()