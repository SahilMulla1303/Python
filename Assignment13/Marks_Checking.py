def marks_cal():
    marks = {"Sahil":[75,87,90,34,55],"Tejal":[65,87,80,78,45],"Kajal":[55,87,70,80,95]}
    a=[]
    b=[]

    for i in marks:
        sums=0
        flag=0
        for j in marks[i]:
            if(j<35):
                flag=1
            sums=sums+j

        per = sums/5
        a.append(i)
        b.append(per)    

        if(flag==1):
            print(i,"Fail")
            
        elif(per>=35 and per<50):
            print(i,"is pass with ",per)
            
        elif(per>=50 and per<60):
            print(i,"is 2nd class with ",per)
            
        elif(per>=60 and per<70):
            print(i,"is 1st class with ",per)
            
        elif(per>=70 and per<=100):
            print(i,"is dict. with ",per)

    print("------------------------------")

    mark_cal = dict(zip(a,b))
    max_marks=max(b)

    for k in mark_cal:

        if(max_marks == mark_cal[k]):
            print("Topper is ",k,"with ", mark_cal[k])

marks_cal()
