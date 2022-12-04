
def String_Sort(*string):
    for i in string:
        c=""
        s=""
        n=""
        ss=""

        for j in i:
            if(ord(j)>=65 and ord(j)<=90):
                c+=j
            elif(ord(j)>=97 and ord(j)<=122):
                s+=j
            elif(ord(j)>=48 and ord(j)<=57):
                n+=j
            elif((ord(j)>=33 and ord(j)<=47) or (ord(j)>=58 and ord(j)<=64) or (ord(j)>=91 and ord(j)<=96)):
                ss+=j
            else:
                print("Some thing wrong")

        total_string = c+s+n+ss
        print(total_string)


String_Sort("tyctcSuuySt78&656gR", "IHG5vtfTTcft%%^7gvvf")
