
def super_prime(n):

    flag=0

    if(n<=0 or n==1):
        flag=2
        
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
        
    if(flag==0):

        if(n>1):
            sum1=0
            flag1=0
            a=str(n)
            for j in a:
                sum1 = sum1 + int(j)

            if(n<=0 or n==1):
                flag1=2
            for k in range(2,sum1):
                if(sum1%k==0):
                    flag1=1
                    break
            if(flag1==0):
                print("Super Prime")
            elif(flag1==2):
                print("Natural no")
            else:
                print("Not Super Prime")
            
    elif(flag==2):
        print("Natural no")
    else:
        print("Not prime")

a=int(input("Enter number :"))
super_prime(a)
