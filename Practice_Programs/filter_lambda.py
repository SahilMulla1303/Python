
lst = [45,76,89,32,11,33,75,80,30]
even = set(filter(lambda i: i%2==0, lst))
odd = tuple(filter(lambda i: i%2!=0, lst))
print(even)
print(odd)
