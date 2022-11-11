
Sub_Marks = []
Sum_Marks = 0
i=0
while(i<5):
    m = int(input("Enter mark of subject :"))
    Sub_Marks.append(m)
    
    i+=1
print("Enterd marks of 5 subject :",Sub_Marks)

i=0
while(i<len(Sub_Marks)):
    Sum_Marks = Sum_Marks + Sub_Marks[i]

    i+=1
print("Total marks :",Sum_Marks)

Per_Marks = (Sum_Marks/len(Sub_Marks))
print("Percentage :",Per_Marks)
    
if(Per_Marks>=75 and Per_Marks<=100):
    print("Pass with distinction")
elif(Per_Marks>=50 and Per_Marks<75):
    print("Pass with First Class")
elif(Per_Marks>=35 and Per_Marks<50):
    print("Pass")
elif(Per_Marks>=0 and Per_Marks<35):
    print("Fail")
else:
    print("Something wrong entered pleas try again")
    
print("Thank You")
