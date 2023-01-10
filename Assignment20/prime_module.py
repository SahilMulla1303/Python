

def prime(n):
    flag=0

    if(n<=0 or n==1):
        flag=2
        
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    return flag
    
if(__name__=="__main__"):
    prime(1)
