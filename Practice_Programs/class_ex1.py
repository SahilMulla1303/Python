class student:

    def marks(self,*m):
        i = 0
        s = 0
        while(i<len(m)):
            s = s + m[i]
            i = i + 1
        return s

s1=student()
r1=s1.marks(67,62,89,87,73)
print(r1)