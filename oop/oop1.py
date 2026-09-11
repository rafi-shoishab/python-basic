class Std:
    def __init__(self, nam, roll, dept): # constructor
        self.name = nam                 # attribute
        self.sub = dept
        self.id = roll

    def show(self):             #method
        print(f"Hi! I am {self.name}, I study {self.sub}, my roll: {self.id}")
  
  
name, roll, dept = input("Enter name, roll, department: ").split()
# Creating object
s1 = Std(name, roll, dept)
s1.show()