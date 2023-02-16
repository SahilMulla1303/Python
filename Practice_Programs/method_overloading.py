class add:
    def sumetion(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            return a+b+c
        elif(a != None and b != None):
            return a + b
        elif (a != None):
            return a

s = add()
print(s.sumetion(20,30,78))
print(s.sumetion(20,30))
print(s.sumetion(20))