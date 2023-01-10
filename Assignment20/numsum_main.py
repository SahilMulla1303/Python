from numsum_module import *

while True:
    a= input("Enter number :")
    final=num_sum(a)
    print(final)
    
    b=input("You want to more num_sum(y/n):")
    if b=="n":
        print("******************************************")
        print("Thank you")
        break
