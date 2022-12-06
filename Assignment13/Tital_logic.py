a= "Hi, i am sahil mulla from bhalawani."

if(ord(a[0])>=97 and ord(a[0])<=122):
            d=ord(a[0])-32
            print(chr(d),end="")
else:
    print(a[0],end="")
    
for i in range(len(a)):
                    
    if(ord(a[i])==32):
        b=i+1
        if(ord(a[b])>=97 and ord(a[b])<=122):
            c=ord(a[b])-32
            print(chr(c),end="")

            
    else: 
        if(i<len(a)-1):
            print(a[i+1],end="")
          


