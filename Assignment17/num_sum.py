
def num_sum(n):

    sum1=0
    sum2=0
    sum3=0
    for i in n:
        a=int(i)
        sum1=sum1+a
        
    n = str(sum1)

    if(len(n)>1):
        for j in n:
            c=int(j)
            sum2=sum2+c
            
        n=str(sum2)
        if(len(n)>1):
        
            for k in n:
                e=int(k)
                sum3=sum3+e
                
            print(sum3)
            
        else:
            print(sum2)
    else:
        print(sum1)
        


a= input("Enter number :")
num_sum(a)
