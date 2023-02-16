# abc - abstract bace class
from abc import ABC,abstractmethod

class demo1(ABC):
    @abstractmethod
    def method1(self):
        pass


class demo2(demo1):
    def method1(self):
        print("S")

d1=demo1()
d=demo2()
d.method1()