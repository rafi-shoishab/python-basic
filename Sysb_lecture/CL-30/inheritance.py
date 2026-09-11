"""Problem 1: Basic Inheritance 
Create a parent class called Animal. 
• Class variables: 
o legs = 4 
o sound = "Some Sound" 
• Method: 
o make_sound() → print the sound 
Create a child class Dog that: 
• Changes sound = "Woof" 
• Does NOT override the method """

class Animal:
    legs = "4"
    sound = "any soud"
    
    def __init__(self, legs, sound):
        self.sound = sound
        self.legs = legs

class Dog(Animal):
    def make_sound(self):
        print(f"sounds like {self.sound}")

obj_dog = Dog("2", "woof")
obj_dog.make_sound()
