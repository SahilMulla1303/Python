def clg(stud):
    def  update():
        stud()
        print("Bhagyashri")
    return update
@clg
def AIT():
    print("Sahil")
    print("Tejal")
    print("Kajal")


AIT()
