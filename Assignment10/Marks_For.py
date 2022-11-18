marks = [80,79,66,59,98]
sum = 0
for i in marks:
    sum = sum + i
    
print("Total Marks is : " , sum)

per = sum/len(marks)
print("Percentage is : " , per)

if(per >= 75 and per < 100):
    print("Distinction")

elif(per >= 60 and per < 75):
    print("First Class")
    
elif(per >= 45 and per < 60):
    print("Second Class")
    
elif(per >= 35 and per < 45):
    print("Pass")

elif(per >= 0 and per < 35):
    print("oops..! You are Fail")
    
else:
    print("Thank you")
