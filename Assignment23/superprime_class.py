class Super_Prime:
    def prime(self,n):
        flag=0
        for i in range(2,n):
            if(n%i==0):
                flag=flag+1
                return False
        return True
    def sup_prime(self,n):
        if(len(str(n))>1):
            flag = 0
            for i in range(2, n):
                if (n % i == 0):
                    flag = flag + 1
                    return False
            return True
        else:
            return False

obj=Super_Prime()
n=int(input("Enter no :"))
p=obj.prime(n)
print("This no is prime       :",p)
sp=obj.sup_prime(n)
print("This no is super prime :",sp)