i=1
j = 1

items = int(input("Enter no of items :"))

items_prices=0

while(i<=items):
    
    while(j<=items):
        items_price = int(input("Enter price item :"))
        items_prices = items_prices + items_price
        j+=1
    print("Total Bill :",items_prices)

    if(items_prices>=5000 and items_prices<7000):
        print("3% dicount on 5000+ amount")
        discount = items_prices * 0.03
        final_amount = items_prices - discount
        print("You save :", discount)
        print("Your final bill amount :", final_amount)
        print()
        item_add = input("You want to add items(Yes/No):")
        print()
        if(item_add=="Yes"):
            No_item_add = int(input("Enter how many item you want to add:"))
            i = items
            items = items+ No_item_add
        elif(item_add=="No"):
            print("Your final bill amount :", final_amount)
            break
        else:
            print("Something wrong entered please try again")
            
    elif(items_prices>=7000 and items_prices<10000):
        print("5% dicount on 7000+ amount")
        discount = items_prices * 0.05
        final_amount = items_prices - discount
        print("You save :", discount)
        print("Your final bill amount :", final_amount)
        print()
        item_add = input("You want to add items(Yes/No):")
        print()
        if(item_add=="Yes"):
            No_item_add = int(input("Enter how many item you want to add:"))
            i = items
            items = items+ No_item_add
        elif(item_add=="No"):
            print("Your final bill amount :", final_amount)
            break
        else:
            print("Something wrong entered please try again")

    elif(items_prices>=10000):
        print("7% dicount on 10000+ amount")
        discount = items_prices * 0.07
        final_amount = items_prices - discount
        print("You save :", discount)
        print("Your final bill amount :", final_amount)
        print()
        item_add = input("You want to add items(Yes/No):")
        print()
        if(item_add=="Yes"):
            No_item_add = int(input("Enter how many item you want to add:"))
            i = items
            items = items+ No_item_add
        elif(item_add=="No"):
            print("Your final bill amount :", final_amount)
            break
        else:
            print("Something wrong entered please try again")            
        
    elif(items_prices>=0 and items_prices<5000):
        print("You have no discount")
        print("Your final bill amount :", items_prices)
        print()
        item_add = input("You want to add items(Yes/No):")
        print()
        if(item_add=="Yes"):
            No_item_add = int(input("Enter how many item you want to add:"))
            i = items
            items = items+ No_item_add
        elif(item_add=="No"):
            print("Your final bill amount :", items_prices)
            break
        else:
            print("Something wrong entered please try again")

    else:
        print("Somethong wromg entered please try again")

i+=1

print("Thank You")
print("Please come again")
