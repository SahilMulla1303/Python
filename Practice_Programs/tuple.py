
#Tuple

a = ("a",6,7.90,33,67,"Sagar",False,6,11,33)
print(type(a))

print(a[5])

print(a[3:8])

print(a[0:7:2])

print(a[5:1:-1])

'''
    In tuple attributes:
        1.index:- for find index in tuple
        2.count:- find how many time value in tuple
'''

print(a.index(6))
print(a.count(6))

a.remove(33)
print(a)
