class samsung():
    def config(self):
        # print("Samsung Galaxy S22")
        # print("6GB RAM")
        # print("128GB ROM")
        return "Hello"
class apple():
    def config(self):
        print("iPhone 14")
        print("6GB RAM")
        print("128GB ROM")
class mobile():
    def data(self,x):
        b = x.config()
        return b

obj1 = mobile()
obj2 = samsung()
a= obj1.data(obj2)
print(a)