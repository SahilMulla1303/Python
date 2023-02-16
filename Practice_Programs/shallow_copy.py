import copy
lst1 = [6,7,3,65,98,23,79,32]
lst2 = copy.copy(lst1)
lst1[2]=33
print(lst1,"\n",lst2)
