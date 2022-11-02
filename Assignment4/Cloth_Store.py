print("")
print("          Wellcome to NAWAB COLLECTION ")
print("---------------------------------------------------")

print("Who want")
print(" 1.For adult \n","2.For kid")
Type = int(input("Please enter your option :"))

# This if for type
if (Type == 1):
    Male_Female = input("Please enter your gender (Male/Female) :")

    print("---------------------------------------------------")
    
# Male-Female section start 

#Male section start
    
    if(Male_Female == "Male"):
        print("What you want :")
        print(" 1.Shirt \n 2.TShirt \n 3.Pant \n 4.Shorts")
        cloth_type = int(input("Please enter what you want (Pleas enter only number):"))
        
        print("---------------------------------------------------")

#Cloth type section start for male
        
        if(cloth_type == 1):
            print("Which type you want")
            print(" 1.Half Sleeve \n 2.Full Sleeve")
            shirt_type = int(input("Please enter which type you want (Pleas enter only number):"))
            
            print("---------------------------------------------------")

#Shirt type section start for male

#HalfSleeve Shirt color start for male
            
            if(shirt_type == 1):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                shirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")

                
                if(shirt_color == 1):
                    print("This shirts are available in our shop")
                    want = input("Please enter you want this shirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")
                        
                elif(shirt_color == 2):
                    print("This shirts are available in our shop")
                    want = input("Please enter you want this shirt(Yes/No):")

                    print("---------------------------------------------------")
                    
                    if(want == "Yes"):
                        print("Your shirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")

                elif(shirt_color == 3):
                    print("This shirts are available in our shop")
                    want = input("Please enter you want this shirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")

                elif(shirt_color == 4):
                    print("This shirts are available in our shop")
                    want = input("Please enter you want this shirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#HalfSleeve Shirt color end for male 

#FullSleeve Shirt color section start for male 

            elif(shirt_type == 2):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                shirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")

                
                if(shirt_color == 1):
                    print("This shirts are available in our shop")
                    want = input("Please enter you want this shirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")
                        
                elif(shirt_color == 2):
                    print("This shirts are available in our shop")
                    want = input("Please enter you want this shirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")

                elif(shirt_color == 3):
                    print("This shirts are available in our shop")
                    want = input("Please enter you want this shirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")

                elif(shirt_color == 4):
                    print("This shirts are available in our shop")
                    want = input("Please enter you want this shirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#HalfSleeve Shirt color section enf for male 
                
            else:
                print("You enter something wrong")

#T-Shirt type section for male start

        elif(cloth_type == 2):
            
            print("Which type you want")
            print(" 1.Half Sleeve \n 2.Full Sleeve \n 3.Sleeveless")
            tshirt_type = int(input("Please enter which type you want (Pleas enter only number):"))

            print("---------------------------------------------------")
            

#T-Shirt type section start for male

#HalfSleeve t-Shirt color start for male
            
            if(tshirt_type == 1):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                shirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")
                
                if(tshirt_color == 1):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")
                        
                elif(shirt_color == 2):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 3):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 4):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#HalfSleeve t-Shirt color end for male 

#FullSleeve t-Shirt color section start for male

            elif(tshirt_type == 2):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                shirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")
 
                if(tshirt_color == 1):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")
                        
                elif(tshirt_color == 2):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 3):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 4):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")
                
                else:
                    print("You enter something wrong")

#FullSleeve t-Shirt color section enf for male

#Sleeveless t-Shirt color start for male
            
            elif(tshirt_type == 3):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                tshirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")
                
                if(tshirt_color == 1):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")
                        
                elif(tshirt_color == 2):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 3):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 4):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#Sleeveless t-Shirt color end for male 
                
            else:
                print("You enter something wrong")

#T-Shirt type section for male end

#Pant section start for male
        elif(cloth_type == 3):
            print("Which type you want")
            print(" 1.Jeans \n 2.Chino \n 3.Cargo")
            pant_type = int(input("Please enter which type you want (Pleas enter only number):"))

            print("---------------------------------------------------")

#Pant type section start for male 
            
            if(pant_type == 1):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                pant_size = int(input("Please enter which size you want (Pleas enter only option number):"))

                print("---------------------------------------------------")

                

#Jeans pant size start for male 
                
                if(pant_size == 1):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")
                        
                elif(pant_size == 2):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 3):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 4):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#Jeans pant size end for male

#Chino pant section start for male

            elif(pant_type == 2):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                pant_size = int(input("Please enter which size you want (Pleas enter only number):"))

                print("---------------------------------------------------")

                

#Chino pant size start for male
 
                if(pant_size == 1):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")
                        
                elif(pant_size == 2):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 3):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 4):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")
                
                else:
                    print("You enter something wrong")

#chino pant size section end for male

#Cargo pant section start for male 
            
            elif(pant_type == 3):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                pant_size = int(input("Please enter which size you want (Pleas enter only option number):"))

                print("---------------------------------------------------")

#Cargo pant size start for male
                
                if(pant_size == 1):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is pant")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")
                        
                elif(pant_size == 2):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 3):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 4):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#Cargo pant size end for male 
                
            else:
                print("You enter something wrong")

#Pant type section end for male

# Shorts section start for male
        elif(cloth_type == 4):
            print("Which type you want")
            print(" 1.Jeans \n 2.Cotton")
            shorts_type = int(input("Please enter which type you want (Pleas enter only number):"))

            print("---------------------------------------------------")

#Shorts type section start for male 
            
            if(shorts_type == 1):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                shorts_size = int(input("Please enter which size you want (Pleas enter only option number):"))

                print("---------------------------------------------------")

                

#Jeans short size start for male 
                
                if(shorts_size == 1):
                    print("This shorts are available in our shop")
                    want = input("Please enter you want this shorts(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shorts is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shorts")
                    else:
                        print("You enter something wrong")
                        
                elif(shorts_size == 2):
                    print("This shorts are available in our shop")
                    want = input("Please enter you want this shorts(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shorts is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shorts")
                    else:
                        print("You enter something wrong")

                elif(shorts_size == 3):
                    print("This shorts are available in our shop")
                    want = input("Please enter you want this shorts(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(shorts_size == 4):
                    print("This shorts are available in our shop")
                    want = input("Please enter you want this shorts(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shorts is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shorts")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#Jeans shorts size end for male

#Cotton shorts section start for male

            elif(shorts_type == 2):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                shorts_size = int(input("Please enter which size you want (Pleas enter only number):"))

                print("---------------------------------------------------")

                

#Cotton shorts size start for male
 
                if(shorts_size == 1):
                    print("This shorts are available in our shop")
                    want = input("Please enter you want this shorts(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shorts is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shorts")
                    else:
                        print("You enter something wrong")
                        
                elif(shorts_size == 2):
                    print("This shorts are available in our shop")
                    want = input("Please enter you want this shorts(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shorts is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shorts")
                    else:
                        print("You enter something wrong")

                elif(shorts_size == 3):
                    print("This shorts are available in our shop")
                    want = input("Please enter you want this shorts(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shorts is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shorts")
                    else:
                        print("You enter something wrong")

                elif(shorts_size == 4):
                    print("This shorts are available in our shop")
                    want = input("Please enter you want this shorts(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your shorts is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shorts")
                    else:
                        print("You enter something wrong")
                
                else:
                    print("You enter something wrong")

#Cotton shorts size section end for male 
            
        else:
            print("You enter something wrong")

#Cloth type section end for male

#Male section end 

#Female section start
            
    elif(Male_Female == "Female"):
        print("What you want :")
        print(" 1.Tops \n 2.TShirt \n 3.Pant \n 4.Leggins")
        cloth_type = int(input("Please enter what you want (Pleas enter only number):"))
        
        print("---------------------------------------------------")

#Cloth type section start for female
        
        if(cloth_type == 1):
            print("Which type you want")
            print(" 1.Half Sleeve \n 2.Full Sleeve")
            tops_type = int(input("Please enter which type you want (Pleas enter only number):"))
            
            print("---------------------------------------------------")

#Tops type section start for female 

#HalfSleeve Tops color start for female
            
            if(tops_type == 1):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                shirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")

                
                if(tops_color == 1):
                    print("This tops are available in our shop")
                    want = input("Please enter you want this tops(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tops is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tops")
                    else:
                        print("You enter something wrong")
                        
                elif(tops_color == 2):
                    print("This tops are available in our shop")
                    want = input("Please enter you want this tops(Yes/No):")

                    print("---------------------------------------------------")
                    
                    if(want == "Yes"):
                        print("Your tops is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tops")
                    else:
                        print("You enter something wrong")

                elif(tops_color == 3):
                    print("This tops are available in our shop")
                    want = input("Please enter you want this tops(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tops is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tops")
                    else:
                        print("You enter something wrong")

                elif(tops_color == 4):
                    print("This tops are available in our shop")
                    want = input("Please enter you want this tops(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tops is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tops")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#HalfSleeve tops color end for male kid

#FullSleeve tops color section start for male kid

            elif(tops_type == 2):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                tops_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")

                
                if(tops_color == 1):
                    print("This tops are available in our shop")
                    want = input("Please enter you want this tops(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tops is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tops")
                    else:
                        print("You enter something wrong")
                        
                elif(tops_color == 2):
                    print("This tops are available in our shop")
                    want = input("Please enter you want this tops(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tops is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tops")
                    else:
                        print("You enter something wrong")

                elif(tops_color == 3):
                    print("This tops are available in our shop")
                    want = input("Please enter you want this tops(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tops is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tops")
                    else:
                        print("You enter something wrong")

                elif(tops_color == 4):
                    print("This tops are available in our shop")
                    want = input("Please enter you want this tops(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tops is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tops")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#HalfSleeve tops color section end for female
                
            else:
                print("You enter something wrong")

#T-Shirt type section for female start

        elif(cloth_type == 2):
            
            print("Which type you want")
            print(" 1.Half Sleeve \n 2.Full Sleeve \n 3.Sleeveless")
            tshirt_type = int(input("Please enter which type you want (Pleas enter only number):"))

            print("---------------------------------------------------")
            

#T-Shirt type section start for female

#HalfSleeve t-Shirt color start for female
            
            if(tshirt_type == 1):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                shirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")
                
                if(tshirt_color == 1):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")
                        
                elif(shirt_color == 2):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 3):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 4):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#HalfSleeve t-Shirt color end for female

#FullSleeve t-Shirt color section start for female

            elif(tshirt_type == 2):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                shirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")
 
                if(tshirt_color == 1):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")
                        
                elif(tshirt_color == 2):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 3):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 4):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type shirt")
                    else:
                        print("You enter something wrong")
                
                else:
                    print("You enter something wrong")

#FullSleeve t-Shirt color section enf for female 

#Sleeveless t-Shirt color start for female
            
            elif(tshirt_type == 3):
                print("Which color you want")
                print(" 1.Black \n 2.Blue \n 3.White \n 4.Red")
                tshirt_color = int(input("Please enter which color you want (Pleas enter only number):"))

                print("---------------------------------------------------")
                
                if(tshirt_color == 1):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")
                        
                elif(tshirt_color == 2):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 3):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                elif(tshirt_color == 4):
                    print("This tshirts are available in our shop")
                    want = input("Please enter you want this tshirt(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type tshirt")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#Sleeveless t-Shirt color end for female
                
            else:
                print("You enter something wrong")

#T-Shirt type section for female end

#Pant section start for female
        elif(cloth_type == 3):
            print("Which type you want")
            print(" 1.Jeans \n 2.Chino \n 3.Cargo")
            pant_type = int(input("Please enter which type you want (Pleas enter only number):"))

            print("---------------------------------------------------")

#Pant type section start for female
            
            if(pant_type == 1):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                pant_size = int(input("Please enter which size you want (Pleas enter only option number):"))

                print("---------------------------------------------------")

                

#Jeans pant size start for female
                
                if(pant_size == 1):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")
                        
                elif(pant_size == 2):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 3):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 4):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#Jeans pant size end for female

#Chino pant section start for female

            elif(pant_type == 2):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                pant_size = int(input("Please enter which size you want (Pleas enter only number):"))

                print("---------------------------------------------------")

                

#Chino pant size start for female
 
                if(pant_size == 1):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")
                        
                elif(pant_size == 2):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 3):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 4):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")
                
                else:
                    print("You enter something wrong")

#chino pant size section end for female

#Cargo pant section start for female
            
            elif(pant_type == 3):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.32 \n 4.36")
                tshirt_color = int(input("Please enter which size you want (Pleas enter only option number):"))

                print("---------------------------------------------------")

#Cargo pant size start for female
                
                if(pant_size == 1):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your tshirt is pant")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")
                        
                elif(pant_size == 2):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 3):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                elif(pant_size == 4):
                    print("This pant are available in our shop")
                    want = input("Please enter you want this pant(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type pant")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#Cargo pant size end for female
                
            else:
                print("You enter something wrong")

#Pant type section end for female

# Leggins section start for female
        elif(cloth_type == 4):
            print("Which type you want")
            print(" 1.Ankle-length \n 2.Knee-length")
            leggins_type = int(input("Please enter which type you want (Pleas enter only number):"))

            print("---------------------------------------------------")

#leggins type section start for female 
            
            if(leggins_type == 1):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                leggins_size = int(input("Please enter which size you want (Pleas enter only option number):"))

                print("---------------------------------------------------")

                

#Ankel-length leggins size start for female 
                
                if(leggins_size == 1):
                    print("This leggins are available in our shop")
                    want = input("Please enter you want this leggins(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your leggins is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type leggins")
                    else:
                        print("You enter something wrong")
                        
                elif(leggins_size == 2):
                    print("This leggins are available in our shop")
                    want = input("Please enter you want this leggins(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your leggins is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type leggins")
                    else:
                        print("You enter something wrong")

                elif(leggins_size == 3):
                    print("This leggins are available in our shop")
                    want = input("Please enter you want this leggins(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your pant is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type leggins")
                    else:
                        print("You enter something wrong")

                elif(leggins_size == 4):
                    print("This leggins are available in our shop")
                    want = input("Please enter you want this leggins(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your leggins is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type leggins")
                    else:
                        print("You enter something wrong")

                else:
                    print("You enter something wrong")

#Ankel-length leggins size end for female

#Knee-length leggins section start for female

            elif(leggins_type == 2):
                print("Which size you want")
                print(" 1.30 \n 2.32 \n 3.34 \n 4.36")
                leggins_size = int(input("Please enter which size you want (Pleas enter only number):"))

                print("---------------------------------------------------")

                

#Knee-length leggins size start for female 
 
                if(leggins_size == 1):
                    print("This leggins are available in our shop")
                    want = input("Please enter you want this leggins(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your leggins is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type leggins")
                    else:
                        print("You enter something wrong")
                        
                elif(leggins_size == 2):
                    print("This leggins are available in our shop")
                    want = input("Please enter you want this leggins(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your leggins is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type leggins")
                    else:
                        print("You enter something wrong")

                elif(leggins_size == 3):
                    print("This leggins are available in our shop")
                    want = input("Please enter you want this leggins(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your leggins is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type leggins")
                    else:
                        print("You enter something wrong")

                elif(leggins_size == 4):
                    print("This leggins are available in our shop")
                    want = input("Please enter you want this leggins(Yes/No):")

                    print("---------------------------------------------------")

                    if(want == "Yes"):
                        print("Your leggins is paked")
                    elif(want == "No"):
                        print("Sorry we dont have any other type leggins")
                    else:
                        print("You enter something wrong")
                
                else:
                    print("You enter something wrong")

#Knee-length leggins size section end for female 
            
        else:
            print("You enter something wrong")

#Cloth type section end for female

#Female section end 
        
    else:
        print("You enter something wrong")
        
# Male-Female section end 
    
elif (Type == 2):
    Male_Female = input("Please enter your gender (Male/Female) :")

    print("---------------------------------------------------")

    if(Male_Female == "Male"):
        print("Shirt-Pant are available \n", "Wich size you want")
        print(" 1.M \n 2.L \n 3.XL")
        male_size = int(input("Please enter which size you watnt(Entrer only option number) :"))

        print("---------------------------------------------------")

        if(male_size == 1):
            print("This Shirt-Pant are available in our shop")
            want = input("Please enter you want this lShirt-Pant(Yes/No):")

            print("---------------------------------------------------")

            if(want == "Yes"):
                print("Your Shirt-Pant is paked")
            elif(want == "No"):
                print("Sorry we dont have any other type Shirt-Pant")
            else:
                print("You enter something wrong")

        elif(male_size == 2):
            print("This Shirt-Pant are available in our shop")
            want = input("Please enter you want this Shirt-Pant(Yes/No):")

            print("---------------------------------------------------")

            if(want == "Yes"):
                print("Your Shirt-Pant is paked")
            elif(want == "No"):
                print("Sorry we dont have any other type Shirt-Pant")
            else:
                print("You enter something wrong")

        elif(male_size == 3):
            print("This Shirt-Pant are available in our shop")
            want = input("Please enter you want this Shirt-Pant(Yes/No):")

            print("---------------------------------------------------")

            if(want == "Yes"):
                print("Your Shirt-Pant is paked")
            elif(want == "No"):
                print("Sorry we dont have any other type Shirt-Pant")
            else:
                print("You enter something wrong")

        
    elif(Male_Female == "Female"):
        print("Frocks are available \n", "Wich size you want")
        print(" 1.M \n 2.L \n 3.XL")
        female_size = int(input("Please enter which size you watnt(Entrer only option number) :"))

        print("---------------------------------------------------")

        if(female_size == 1):
            print("This Frocks are available in our shop")
            want = input("Please enter you want this Frocks(Yes/No):")

            print("---------------------------------------------------")

            if(want == "Yes"):
                print("Your Frockst is paked")
            elif(want == "No"):
                print("Sorry we dont have any other type Frocks")
            else:
                print("You enter something wrong")

        elif(female_size == 2):
            print("This Frocks are available in our shop")
            want = input("Please enter you want this Frocks(Yes/No):")

            print("---------------------------------------------------")

            if(want == "Yes"):
                print("Your Frocks is paked")
            elif(want == "No"):
                print("Sorry we dont have any other type Frocks")
            else:
                print("You enter something wrong")

        elif(female_size == 3):
            print("This Frocks are available in our shop")
            want = input("Please enter you want this Frocks(Yes/No):")

            print("---------------------------------------------------")

            if(want == "Yes"):
                print("Your Frocks is paked")
            elif(want == "No"):
                print("Sorry we dont have any other type Frocks")
            else:
                print("You enter something wrong")
        

    else:
        print("You enter wrong option")
    
else:
    print("You enter wrong option")

print("Thank You")
print("Please come again")
print("---------------------------------------------------")
