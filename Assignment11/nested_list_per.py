marks = [[56,78,45,49,54],[66,78,95,41,54],[86,78,95,49,64],[86,78,85,49,40]]

marks_sum=[]
marks_per=[]
for i in marks:
    sum=0
    for j in i:
        sum = sum + j
    per = sum/len(i)
    marks_per.append(per)
    
    marks_sum.append(sum)
    
print("Sum list :",marks_sum)
print("Percentage list :",marks_per)
