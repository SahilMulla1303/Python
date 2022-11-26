a = input("Enter string to sort :")

for i in a:
    if(ord(i)>=65 and ord(i)<=90):
        print(i,end="")

for i in a:
    if(ord(i)>=97 and ord(i)<=122):
        print(i,end="")

for i in a:
    if(ord(i)>=48 and ord(i)<=57):
        print(i,end="")

for i in a:
    if((ord(i)>=33 and ord(i)<=47) or (ord(i)>=58 and ord(i)<=64)):
        print(i,end="")
