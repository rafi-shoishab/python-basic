"""Problem 4: Access Parent Method from Child 
Create parent class Math. 
• add() → print sum of 5 and 10 
Create child class AdvancedMath. 
• Override add() 
• Inside it: 
o First call parent add() using super() 
o Then print multiplication of 5 and 10 
Expected Output: 
15 
50 
"""

class Math:
    x = 10
    y = 5
    def add(self, x, y):
        self.x = x
        self.y = y
        print (f{self.x} + {self.y})

class Adv(Math):
    def __init__(self):
        super().__init__()