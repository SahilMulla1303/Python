class String_Sort:
    def String(self,a):
        c = ""
        s = ""
        n = ""
        ss = ""

        for i in a:
            if (ord(i) >= 65 and ord(i) <= 90):
                c += i
            elif (ord(i) >= 97 and ord(i) <= 122):
                s += i
            elif (ord(i) >= 48 and ord(i) <= 57):
                n += i
            elif ((ord(i) >= 33 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64) or (
                    ord(i) >= 91 and ord(i) <= 96)):
                ss += i
            else:
                print("Some thing wrong")

        total_string = c + s + n + ss
        return total_string

obj=String_Sort()
a=input("Enter string :")
s1=obj.String(a)
print("Sorted String :",s1)