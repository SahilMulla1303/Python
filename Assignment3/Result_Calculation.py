print("                 Result Calculation                ")
print("---------------------------------------------------")

print("Enter Obtained Marks & Max marks of all subjects")

sub1 = int(input("Enter obtained marks in Marathi : "))
Max_sub1 = int(input("Enter max marks of Marathi : "))

sub2 = int(input("Enter obtained marks in Hindi : "))
Max_sub2 = int(input("Enter max marks of Hindi : "))

sub3 = int(input("Enter obtained marks in English : "))
Max_sub3 = int(input("Enter max marks of English : "))

sub4 = int(input("Enter obtained marks in Math's : "))
Max_sub4 = int(input("Enter max marks of Math's : "))

sub5 = int(input("Enter obtained marks in Science : "))
Max_sub5 = int(input("Enter max marks of Science : "))

sub6 = int(input("Enter obtained marks in History : "))
Max_sub6 = int(input("Enter max marks of History : "))

sub7 = int(input("Enter obtained marks in Geography : "))
Max_sub7 = int(input("Enter max marks of Geography : "))

Total_Marks_Obtained = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7
print("Total marks obtained in exam :",Total_Marks_Obtained)

Max_Marks = Max_sub1 + Max_sub2 + Max_sub3 + Max_sub4 + Max_sub5 + Max_sub6 + Max_sub7
print("Max marks in exam :",Max_Marks)

per = (Total_Marks_Obtained / Max_Marks) * 100
print("Percentage of marks in exam :",per,"%")
