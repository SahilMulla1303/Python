
marks = [[56,78,45,49,54],[66,78,95,41,54],[86,78,95,49,64],[86,78,85,49,40]]

marks_sum=[]

i=0
sum = 0
while(i<len(marks)):
    j=0
    while(j<len(marks[i])):
        
        sum = sum + marks[i][j]
        
        j+=1
        
    marks_sum.append(sum)
    
    i+=1
    
print("Sumetion of marks :",marks_sum)
