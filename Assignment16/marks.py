
def marks(*m):
    for i in m:
        sums=0
        flag=0
        for j in i:
            if(j<35):
                flag=flag+1
            sums=sums+j

        per = sums/5   

        if(flag==1 or flag==2):
            print(i,"is atkt with ",per)
        elif(flag>2):
            print(i,"Fail")
        elif(per>=35 and per<50):
            print(i,"is pass with ",per)
            
        elif(per>=50 and per<60):
            print(i,"is 2nd class with ",per)
            
        elif(per>=60 and per<70):
            print(i,"is 1st class with ",per)
            
        elif(per>=70 and per<=100):
            print(i,"is dict. with ",per)


marks([56,78,89,65,45],[67,65,25,12,19],[60,83,18,90,62],[45,67,76,72,70],[89,82,67,56,48])
