
def max_number(*n):
    
    a=n[0]
    for i in n:
        if(i>a):
            a = i
    print(a)

max_number(34,67,21,388,46,99,222,56,43,67)
