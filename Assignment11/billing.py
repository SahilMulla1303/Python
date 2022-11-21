
Product_Price_Sum = 0
Product_List = []

for i in range(1001):
    Product_Price = int(input("Enter product price :"))
    
    Product_List.append(Product_Price)
    
    Product_Price_Sum = Product_Price_Sum + Product_Price
    print("Total :",Product_Price_Sum)
    add = input("Do you want add product?(Y/N) ")
    if(add == "N"):
        print("Product prices list :",Product_List)
        Remove_Item = input("Do you want remove product?(Y/N) ")
        if(Remove_Item == "Y"):
            No_Remove_Item = int(input("Enter how may number you want to remove :"))

            for k in range(No_Remove_Item):
                Item_No = int(input("Enter price of item you want to remove :"))
               
                Product_List.remove(Item_No)

                sums = 0
                for j in Product_List:
                    sums += j
                   
            print("New Product prices list :",Product_List)
            print("New Total :",sums)
            break
        else:
            print("Product prices list :",Product_List)
            print("Total :",Product_Price_Sum)
            break

if (Product_Price_Sum >= 1000 and Product_Price_Sum < 1500):
    print("2% dicount on 1000+ amount")
    discount = Product_Price_Sum * 0.02
    final_amount = Product_Price_Sum - discount
    print("You save :", discount)
    print("Your final bill amount :", final_amount)
elif (Product_Price_Sum >= 1500 and Product_Price_Sum < 2000):
    print("3% dicount on 1500+ amount")
    discount = Product_Price_Sum * 0.03
    final_amount = Product_Price_Sum - discount
    print("You save :", discount)
    print("Your final bill amount :", final_amount)
elif (Product_Price_Sum >= 5000):
    print("5% dicount on 5000+ amount")
    discount = Product_Price_Sum * 0.05
    final_amount = Product_Price_Sum - discount
    print("You save :", discount)
    print("Your final bill amount :", final_amount)
elif(Product_Price_Sum <= 1000):
    print("You have no discount on bill")
else:
    print("Something wrong")

    
