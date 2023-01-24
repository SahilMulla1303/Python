class clg:
    def __init__(self):
        self.clg_name = "AITRC"
        self.clg_address = "Vita"
        self.branches = "5"
        self.chairman = "Adv. Vaibhav Sadashivrao Patil"

    def clg_details(self):
        print("College name :",self.clg_name,"\nCollege address :",self.clg_address,"\nBranches :",self.branches,"\nChairman :",self.chairman)
class dep(clg):
    def __init__(self):
        self.dep_name = "CSE"
        self.dep_hod = "C. .Shinde"
        self.dep_classes = "4"
        clg.__init__(self)
    def dep_details(self):
        print("Department Name :",self.dep_name,"\nH.O.D :",self.dep_hod,"\nTotal Classes :",self.dep_classes)
class stud(dep):
    def __init__(self):
        self.stud_name = "Sahil Mulla"
        self.stud_no = "3010"
        dep.__init__(self)
    def stud_details(self):
        print("Student Name :",self.stud_name,"\nRoll No :",self.stud_no,"\nDepartment Name :",self.dep_name,"\nCollege name :",self.clg_name,",",self.clg_address)

obj = stud()
obj.stud_details()