class comp:

    def __init__(self):
        self.comp = "Google"
        self.ceo = "Sunder Pichai"
        self.founder = "Larry Page, Sergey Brin"
        self.founded = "September 4 1998"
        self.net_worth = "Rs. 95 Lakh Crore"
        self.headquarter = "California, US"


    def details(self):
        print("Cpmpany Details")
        print()
        print("Company name :",self.comp,"\nCEO name :",self.ceo,"\nFounder name :",self.founded,"\nFounded :",self.founded,"\nNet Worth :",self.net_worth,"\nHeadquarter :",self.headquarter)
        print("--------------------------")
    class comp_ceo():
        def __init__(self):
            self.name = "Sunder Pichai"
            self.country = "India"
            self.dob = "June 10 1972"
            self.age = "50"
            self.title= "CEO of Alphabet and Google"

        def ceo_details(self):
            print("CEO Details")
            print()
            print("Name :",self.name,"\nCountry :",self.country,"\nD.O.B :",self.dob,"\nAge :",self.age,"\nTitle :",self.title)


c1 = comp()
c1.details()
a = c1.comp_ceo()
a.ceo_details()