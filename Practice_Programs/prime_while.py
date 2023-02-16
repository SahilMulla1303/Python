
n = int(input("Tack no:"))

flag=0
i=2
if(n<=0 or n==1):
    flag=2
while(i<n):
    if(n%i==0):
        flag=1
        break        
    i=i+1
if(flag==0):
    print("prime")
elif(flag==2):
    print("Natural no")
else:
    print("Not prime")
