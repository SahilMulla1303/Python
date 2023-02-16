class book:

    def __init__(self):
        self.book = "Harry Potter"
        self.author = "J.K.Rowling"
        self.price = "2000Rs"
        self.publisher = "Bloomsbury"
        self.parts = "8"
    def details(self):
        print(self.book,self.author,self.price,self.publisher,self.parts)

    class book_author:
        def __init__(self):
            self.name = "J.K.Rowling"
            self.country = "UK"
            self.age = "53"
            self.dob = "23/09/1979"
        def author_details(self):
            print(self.name,self.country,self.age,self.dob)


b1 = book()
b1.details()
a = b1.book_author()
a.author_details()