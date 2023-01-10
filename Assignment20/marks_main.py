from marks_module import *

while True:
    marks_list=[]
    for j in range(1,6):
        a=int(input("Enter subject marks :"))
        marks_list.append(a)
        
    per,flag=marks_sum(marks_list)

    if(flag==1 or flag==2):
        print("ATKT with ",per)
    elif(flag>2):
        print("Fail")
    elif(per>=35 and per<50):
        print("Pass with ",per)
    elif(per>=50 and per<60):
        print("2nd class with ",per)  
    elif(per>=60 and per<70):
        print("1st class with ",per)                
    elif(per>=70 and per<=100):
        print("dict. with ",per)

    print()
    b=input("You want to calculate more student marks?(y/n)")
    print()
    if(b=="n"):
        print("Thank You")
        break
