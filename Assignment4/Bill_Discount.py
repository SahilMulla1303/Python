amount = float(input("Enter your bill amount :"))

if (amount >= 1000 and amount < 1500):
    print("2% dicount on 1000+ amount")
    discount = amount * 0.02
    final_amount = amount - discount
    print("You save :", discount)
    print("Your final bill amount :", final_amount)
elif (amount >= 1500 and amount < 2000):
    print("3% dicount on 1500+ amount")
    discount = amount * 0.03
    final_amount = amount - discount
    print("You save :", discount)
    print("Your final bill amount :", final_amount)
elif (amount >= 5000):
    print("5% dicount on 5000+ amount")
    discount = amount * 0.05
    final_amount = amount - discount
    print("You save :", discount)
    print("Your final bill amount :", final_amount)
