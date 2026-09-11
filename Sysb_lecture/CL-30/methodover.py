"""Problem 2: Method Overriding 
Create a parent class Calculator. 
• x = 10 
• y = 5 
• Method calculate() → print x + y 
Create a child class AdvancedCalculator. 
• x = 10 
• y = 5 
• Override calculate() → print x * y 
Task: 
1. Create object of AdvancedCalculator 
2. Call calculate() 
3. What will be the output? 
"""

class Calculator:
    x = 10
    y = 5
    def clac(self, x, y):
        print(f'{x+y}')
        
class Adv(Calculator):
    def clac(self, x, y):
        print(f'{x * y}')


obj_1 = Adv()
obj_1.clac(obj_1.x, obj_1.y)
