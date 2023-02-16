class laptop():
    def __init__(self):
        self.comp="HP"
        self.pro="intel i3"
        self.ram="4 GB"
        self.rom="512 ssd"
        self.screen="14 in"

    def config(self):
        print("Company   :",self.comp)
        print("Processor :",self.pro)
        print("Ram       :",self.ram)
        print("Rom       :",self.rom)
        print("Display   :",self.screen)

l1=laptop()
l2=laptop()
l1.config()
print("---------------------")
l2.pro="i5"
l2.ram="8 GB"
l2.config()


