
def marks_cal(**marks):
     
    a=[]
    b=[]

    f=open("student.txt","w")
    f.write("Name")
    f.write("\t")
    f.write("Total")
    f.write("\t")
    f.write("Per")
    f.write("\t")
    f.write("Class")
    f.write("\n")
    f.write("------------------------------")
    f.write("\n")
    for i in marks:
        sums=0
        flag=0
        for j in marks[i]:
            if(j<35):
                flag=flag+1
            sums=sums+j

        per = sums/5
        a.append(i)
        b.append(per)    

        if(flag==1 or flag==2):
            print(i,sums,per,"ATKT")
            f.write(i)
            f.write("\t")
            f.write(str(sums))
            f.write("\t")
            f.write(str(per))
            f.write("\t")
            f.write("ATKT")
            f.write("\n")
        elif(flag>2):
            print(i,sums,per,"Fail")
            f.write(i)
            f.write("\t")
            f.write(str(sums))
            f.write("\t")
            f.write(str(per))
            f.write("\t")
            f.write("Fail")
            f.write("\n")
        elif(per>=35 and per<50):
            print(i,sums,per,"pass")
            f.write(i)
            f.write("\t")
            f.write(str(sums))
            f.write("\t")
            f.write(str(per))
            f.write("\t")
            f.write("Pass")
            f.write("\n")
            
        elif(per>=50 and per<60):
            print(i,sums,per,"2nd")
            f.write(i)
            f.write("\t")
            f.write(str(sums))
            f.write("\t")
            f.write(str(per))
            f.write("\t")
            f.write("2nd")
            f.write("\n")
            
        elif(per>=60 and per<70):
            print(i,sums,per,"1st")
            f.write(i)
            f.write("\t")
            f.write(str(sums))
            f.write("\t")
            f.write(str(per))
            f.write("\t")
            f.write("1st")
            f.write("\n")
            
        elif(per>=70 and per<=100):
            print(i,sums,per,"Dict.")
            f.write(i)
            f.write("\t")
            f.write(str(sums))
            f.write("\t")
            f.write(str(per))
            f.write("\t")
            f.write("Dict.")
            f.write("\n")
        print("------------------------------")
        f.write("------------------------------")
        f.write("\n")

    print("------------------------------")
    f.write("------------------------------")
    f.write("\n")

    mark_call = dict(zip(a,b))
    max_marks=max(b)

    for k in mark_call:

        if(max_marks == mark_call[k]):
            print("Topper is ",k,"with ", mark_call[k])
            f.write("Topper is ")
            f.write(" ")
            f.write(str(k))
            f.write(" ")
            f.write("with")
            f.write(" ")
            f.write(str(mark_call[k]))
            f.write("\n")

marks_cal(Sahil=[75,87,90,34,55],Tejal=[65,87,80,78,45],Kajal=[55,17,70,10,34])
