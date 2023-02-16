def no_swap(sub):
    def  update(a,b):
        if a<b:
            a,b=b,a
            sub(a,b)
        else:
            sub(a,b)
    return update

@no_swap
def substraction(a,b):
    print(a-b)

substraction(7,30)
