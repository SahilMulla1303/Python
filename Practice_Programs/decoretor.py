def AIT():
    print("Sahil")
    print("Tejal")
    print("Kajal")

def clg(stud):
    def  update():
        stud()
        print("Bhagyashri")
    return update

AIT = clg(AIT)
AIT()
