from sort_module import *


while True:
    a=input("Enter string for sort :")
    sort=String_Sort(a)
    print(sort)

    print()
    b=input("You want to more string sort(y/n):")
    print()
    if b=="n":
        print("******************************************")
        print("Thank you")
        break
