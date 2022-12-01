
def add():
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c = a + b
    return c
def sub():
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c = a - b
    return c
def mul():
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c = a * b
    return c
def div():
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c = a / b
    return c
def mod():
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c = a % b
    return c

d = input("Enter which operation you want to execute (+,-,*,/,%) :")

if(d=="+"):
    e = add()
    print(e)
elif(d=="-"):
    e = sub()
    print(e)
elif(d=="*"):
    e = mul()
    print(e)
elif(d=="/"):
    e = div()
    print(e)
elif(d=="%"):
    e = mod()
    print(e)
else:
    print("Somthing wrong try again")




    
