lst = [34,56,87,12,45,4,90]
a=lst[0]
for i in range(1,len(lst)):
    if(lst[i]>a):
        a=lst[i]
print(a)
