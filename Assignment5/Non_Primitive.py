
print("---------- List ----------")

lst = [23,3.14,57,"Sahil",True,7,3.14]
print(lst)

print()

print("Print using indexing :", lst[3])
print("Print using reverse_indexing :", lst[-3])

print("Print start to 3 index element using slicing :",lst[:4])
print("Print 0 to 3 index element using slicing :",lst[0:4])

print("Print 4 to end index element using slicing :",lst[4:])
print("Print 0 to 3 index element using slicing :",lst[4:6])

print("Print 1 to 5 index element with diff. 2 using slicing :",lst[1:6:2])

print("Print reverse list using slicing :",lst[::-1])

print("Print reverse list 0 to 3 index element using slicing :",lst[3:0:-1])


print("Index of entered element:",lst.index(57))
print("Count of entered element in list:",lst.count(3.14))

lst.append(33)
print("Add element in list at end:",lst)

lst.insert(3,78)
print("Add elemet in list at 3rd index position :",lst)

a = [0,1,2,3,4]
lst.extend(a)
print("Add other list at end of list: ",lst)

lst.remove(3.14)
print("Remove elment from list:",lst)

lst.pop(3)
print("Remove 3rd index elemet from list :",lst)

lst.reverse()
print("Print reverse list:",lst)

lst1 = [34,78,64,90,12]
lst1.sort()
print("Print sorted list in ascending order :",lst1)

lst1.clear()
print("Clear the list elements:",lst1)

print()
print("----------- Tuple ----------")

tup = (34,56,"Sahil",3.14,True,78,3.14)
print(tup)

print("Index of entered element:",tup.index(56))
print("Count of entered element in tuple:",tup.count(3.14))

print()
print("----------- Dictionary ----------")

dic = {1:"sahil", 2:45, 3:True, 4:3.14}
print(dic)

print("Print only keys from dictionary :",dic.keys())
print("Print only values from dictionary :",dic.values())

print()
print("----------- Set ----------")

st = {23,3.14,57,"Sahil",True,7}
print(st)


print()
print("----------- Nested ----------")

lis = [45,67,"Sahil",True, [70,50,55,78], 99,45,89,100,56]
print("Nested list :",lis)
print(type(lis[4]),lis[4],type(lis[4][2]), lis[4][2])

tp = [45,67,"Sahil",True, (70,50,55,78), 99,45,89,100,56]
print("tupel in list nrsted :",tp)
print(type(tp[4]),tp[4],type(tp[4][2]), tp[4][2])


print()
print("----------- TypeCasting ----------")

a = (34,78,90,54,10,56)
print(a,type(a))

b = list(a)
print("Tuple to List:",b,type(b))

c = set(b)
print("List to set:",c,type(c))

print("Two list to one dictionary type casting:")
a = [1,2,3,4,5]
b = ["Sahi",True,34,78,3.14]

x = zip(a,b)
print(x)
y = dict(x)
print(y)

print(dict(zip(a,b)))






















