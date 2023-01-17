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
class comp_ceo(comp):
    def __init__(self):

        self.country = "India"
        self.dob = "June 10 1972"
        self.age = "50"
        self.title= "CEO of Alphabet and Google"
        comp.__init__(self)

    def ceo_details(self):
        print("CEO Details")
        print()
        print("Name :",self.ceo,"\nCountry :",self.country,"\nD.O.B :",self.dob,"\nAge :",self.age,"\nTitle :",self.title)



a = comp_ceo()
a.details()
a.ceo_details()