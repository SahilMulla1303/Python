mark = [45,89,67,34,23,92,10,67,7]

pass_stud = list(filter(lambda i: i>=35, mark))
fail_stud = list(filter(lambda i: i<35, mark))
print(pass_stud)
print(fail_stud)
