
a=7
flag=0
for i in range(2,a):
    prime= lambda i : flag=1 if(a%i==0)
    prime(a)
b = lambda flag : "prime" if(flag=0) 
print(b())
