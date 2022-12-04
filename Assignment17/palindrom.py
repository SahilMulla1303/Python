
def palindrom(s):

    rev = s[::-1]
    if(s == rev):
        print("Palindrom")
    else:
        print("Not Palindrom")


a=input("Enter :")
palindrom(a)
