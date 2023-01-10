def marks_sum(m):
    sums=0
    flag=0
    for i in m:
        if(i<35):
            flag=flag+1
            
        sums=sums+i
    per = sums/len(m)
    
    return per,flag

            
if(__name__ == "__main__"):

    marks_sum([1])
