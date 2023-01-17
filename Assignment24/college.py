class college:
    def __init__(self):
        self.clg_name = "Adarsh Institute Of Technology and Resurch Center"
        self.address = "Vita, Maharashtra"
        self.branches = "5"
        self.chairman = "Adv. Vaibhav Sadashivrao Patil"
    def clg_detail(self):
        print("College info")
        print()
        print("College name :",self.name,"\nAddress :",self.address,"\nBranches No :",self.branches,"\nChairman",self.chairman)
        print("-------------------------------")

class student(college):
    def __init__(self):
        self.stud_name = "Sahil Mulla"
        self.address = "Bhalawani"
        self.dob = "March 13 2002"
        self.branch = "CSE"
        college.__init__(self)
    def stud_info(self):
        print("Student info")
        print()
        print("Student Name :",self.stud_name,"\nAddress :",self.address,"\nD.O.B :",self.dob,"\nCollege :",self.clg_name,"\nBranch :",self.branch)

s = student()
s.stud_info()