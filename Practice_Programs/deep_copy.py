import copy
lst1 = [[6,7,3],[65,98,23],[79,32]]
lst2 = copy.deepcopy(lst1)
lst1[0][2]=33
print(lst1,"\n",lst2)
