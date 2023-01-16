class Marks_Cal:
    def marks(self,**m):

        a = []
        b = []

        for i in m:
            sums = 0
            for j in m[i]:
                sums = sums + j
            per = sums / 5
            a.append(i)
            b.append(per)

            print(i,"   ",sums,"   ", per)

        mark_cal = dict(zip(a, b))

        return a,b

    def max_marks(self,b):
        max = b[0]
        for i in b:
            if max < i:
                max = i
        return b.index(max)

    def min_marks(self, b):
        min = b[0]
        for i in b:
            if min > i:
                min = i
        return b.index(min)

obj1=Marks_Cal()

print("Name     Total     Per")

a,b=obj1.marks(Sahil=[75,87,90,35,55],Ajit=[65,87,80,78,55],Rishad=[55,37,70,40,34],Pratik=[65,77,82,68,35])

m2=obj1.max_marks(b)
m3=obj1.min_marks(b)

print("------------------------------")
print("------------------------------")
print("Topper is ",a[m2]," with ",b[m2])
print("------------------------------")
print("------------------------------")
print("Min is ",a[m3]," with ",b[m3])