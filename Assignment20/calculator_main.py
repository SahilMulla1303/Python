from calculator_module import *

print("Calculator oprations : \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n 5.Modulus \n 6.Fractional Division \n 7.Power")
c=int(input("Enter no of which opration want to calculate :"))

a=int(input("Enter 1st No :"))
b=int(input("Enter 2nd No :"))
if(c==1):
    print("Addition of numbers is", add(a,b))
elif(c==2):
    print("Subtraction of numbers is", sub(a,b))
elif(c==3):
    print("Multiplication of numbers is", mul(a,b))
elif(c==4):
    print("Division of numbers is", div(a,b))
elif(c==5):
    print("Modulus of numbers is", mod(a,b))
elif(c==6):
    print("Floor division of numbers is", fDiv(a,b))
elif(c==7):
    print("Result using arithmetic operator is", power(a,b))
