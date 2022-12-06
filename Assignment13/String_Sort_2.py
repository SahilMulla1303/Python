
string = input("Enter string for sort :")
c=""
s=""
n=""
ss=""

for i in string:
    if(ord(i)>=65 and ord(i)<=90):
        c+=i
    elif(ord(i)>=97 and ord(i)<=122):
        s+=i
    elif(ord(i)>=48 and ord(i)<=57):
        n+=i
    elif((ord(i)>=33 and ord(i)<=47) or (ord(i)>=58 and ord(i)<=64)):
        ss+=i
    else:
        print("Some thing wrong")

total_string = c+s+n+ss
print(total_string)
