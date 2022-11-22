
n = int(input("Tack no:"))

flag=0

if(n<=0 or n==1):
    flag=2
    
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
    
if(flag==0):
    print("prime")
elif(flag==2):
    print("Natural no")
else:
    print("Not prime")
