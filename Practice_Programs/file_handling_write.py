'''
a= open("demo.txt","w")
a.write("This is sahil mulla")
a.close()
'''

x=[5,67,87,"ss",78]
a= open("demo.txt","w")
#w is write
for i in x:
    a.write(str(i))
    a.write("\n")
a.close()

a= open("demo.txt","a")
#a(in open)=append 
for i in range(1,21):
    a.write(str(i))
    a.write("\n")
a.close()


a= open("demo.txt","r")
print(a.read())
