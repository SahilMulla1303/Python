marks = [45,78,90,[67,79,568,628,72,89,90],436,32,19,89,(234,890,32),67,[54,823,789],67,90,7.55]

sum = 0
for i in range(len(marks)):
    
    list_type =type(marks[i])
    
    if(list_type == int or list_type == float):
        
        sum = sum+marks[i]
        
    elif(list_type == list or list_type == tuple):
        
        for j in range(len(marks[i])):
            
            sum = sum + marks[i][j]
        
    
print("Sumetion of marks :",sum)
