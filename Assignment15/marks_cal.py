
def marks_add():

    marks = [[78,98,70,84,91],[78,88,60,84,71],[58,98,64,84,39],[68,70,48,84,51],[44,97,40,64,91]]
    
    marks_sum = []
    for i in marks:
        marks_s=0
        for j in i:
            marks_s = marks_s + j

        marks_sum.append(marks_s)
    
    return marks_sum


a=marks_add()

marks_per = []

for k in a:
    per = k/5
    marks_per.append(per)
    

print(marks_per)

