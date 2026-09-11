class Car:
    def __init__(self, brand, model, year): #constructor
        self.brnd = brand        #attribute
        self.modl = model        #attribute
        self.yr = year           #attribute
        
    def display(self): #method
        print(f"ur car: {self.brnd}, {self.modl}, {self.yr}")

# nam, mdl, yr = input("enter: ").split()
#object 
c1 = Car('Toyota', 'Aqua', '2018')
c2 = Car('Mitshubisi', 'Xpander', '2020')
c1.display()
c2.display()