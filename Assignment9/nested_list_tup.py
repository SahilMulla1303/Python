marks = [45,78,90,[67,79,568,628,72,89,90],436,32,19,89,(234,890,32),67,[54,823,789],67,90,7.55]

i=0
sum = 0
while(i<len(marks)):
    
    list_type = str(type(marks[i]))
    
    if(list_type == "<class 'int'>" or list_type == "<class 'float'>"):
        
        sum = sum+marks[i]
        
    elif(list_type == "<class 'list'>" or list_type == "<class 'tuple'>"):
        
        j=0
        while(j<len(marks[i])):
            
            sum = sum + marks[i][j]
            
            j+=1
    i+=1
    
print("Sumetion of marks :",sum)
