from prime_module import *

n = int(input("Tack no:"))
a=prime(n)
if(a==0):
    print("prime")
elif(a==2):
    print("Natural no")
else:
    print("Not prime")
