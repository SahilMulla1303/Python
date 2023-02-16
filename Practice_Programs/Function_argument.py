def add(a,b=0):
    c=a+b
    return c

s=add(3)
print(s)


def add(a,b):
    c=a+b
    return c

s=add(3,5)
print(s)

def num(a,*b):
    print(a,b)

num(34,56,43,67)
