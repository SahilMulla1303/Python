i=0
Product_Price_Sum = 0
Product_List = []
while(i < 1000):
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
            k=0
            while(k < No_Remove_Item):
                Item_No = int(input("Enter price of item you want to remove :"))
               
                Product_List.remove(Item_No)
                j=0
                sums = 0
                while(j < len(Product_List)):
                    sums += Product_List[j]
                    j+=1
                k+=1
            print("New Product prices list :",Product_List)
            print("New Total :",sums)
            break
        else:
            print("Product prices list :",Product_List)
            print("Total :",Product_Price_Sum)
            break
    i+=1

    
