

per = lambda a: "Dist." if(a>=75 and a<=100) else "First class" if(a<75 and a>=65) else "Second Class" if(a>=50 and a<65) else "Pass" if(a>=35 and a<50) else "fail" if(a>=0 and a<35)else "wrong per insered"
print(per(80))
print(per(65))
print(per(50))
print(per(40))
print(per(30))
print(per(800))

