"""Problem 3: Constructor Inheritance 
Create a parent class Person. 
• Constructor prints: "I am a Person" 
Create a child class Student that does NOT define its own constructor. 
Task: 
1. Create object of Student 
2. What will be printed? 
3. Why?"""

class Person:
    def __init__(self, type="person"):
        self.type = type
        print(f"I am a {self.type}")
class Student(Person):
    def __init__(self):
        super().__init__("student")

class Worker(Person):
    def __init__(self):
        super().__init__("worker")

std = Student()
wrk = Worker()