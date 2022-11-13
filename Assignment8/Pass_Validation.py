Pass = input("Enter Password :")

capital = 0
small = 0
num = 0
symbol = 0
if(len(Pass)>=8):
    i=0
    while(i<len(Pass)):
        if(ord(Pass[i])>=65 and ord(Pass[i])<=90):
            capital = 1
        elif(ord(Pass[i])>=97 and ord(Pass[i])<=122):
            small = 1
        elif(ord(Pass[i])>=48 and ord(Pass[i])<=57):
            num = 1
        elif(Pass[i]=="@" or Pass[i]=="#" or Pass[i]=="$" or Pass[i]=="&" or Pass[i]=="%" or Pass[i]=="*"):
            symbol = 1
        i+=1
    if(capital==1 and small == 1 and num == 1 and symbol == 1):
        print("Valid Password")
    elif(capital==0 and small == 1 and num == 1 and symbol == 1):
        print("Minimum 1 Capital letter require")
    elif(capital==1 and small == 0 and num == 1 and symbol == 1):
        print("Minimum 1 Small letter require")
    elif(capital==1 and small == 1 and num == 0 and symbol == 1):
        print("Minimum 1 Number require")
    elif(capital==1 and small == 1 and num == 1 and symbol == 0):
        print("Minimum 1 Spacial Symbol require(@,#,$,&,%,*)")
    else:
        print("Invalid Password")
else:
    print("Invalid Password(Minimum 8 characters required)")
