class cse():
    def Result(self):
        print("1st year marks of student is 79%")
        print("2nd year marks of student is 80%")
        print("3rd year marks of student is 75%")
        print("B-tech of the marks is 95%")

class entc():
    def Result(self):
        print("1st year marks of student is 72%")
        print("2nd year marks of student is 75%")
        print("3rd year marks of student is 85%")
        print("B-tech of the marks is 87%")

class mech():
    def Result(self):
        print("1st year marks of student is 82%")
        print("2nd year marks of student is 65%")
        print("3rd year marks of student is 80%")
        print("B-tech of the marks is 91%")

class civil():
    def Result(self):
        print("1st year marks of student is 82%")
        print("2nd year marks of student is 65%")
        print("3rd year marks of student is 81%")
        print("B-tech of the marks is 97%")

class Department():
    def percentage(self,x):
        x.Result()

d = Department()
c = cse()
e = entc()

d.percentage(e)
print()
d.percentage(c)
