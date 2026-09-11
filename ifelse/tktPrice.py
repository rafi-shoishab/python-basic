"""Ticket Pricing System
Ticket prices:
Children (<12): $5
Teens (12-17): $8
Adults (18-64): $12
Seniors (65+): $7
Apply a 10% discount if today is "Monday"."""


print("===Ticket Price===")
print("Children (<12): $5")
print("Teens (12-17): $8")
print("Adults (18-64): $12")
print("Seniors (65+): $7")
while True:
    name = input("enter ur nickname: ").capitalize()
    age = int(input("enter ur age: "))
    day = input("enter day: ").lower()
    num = int(input("enter no. of tickets you want to buy: "))

    if age<12 and day != "monday":
        price = 5*num
    elif age>12 and age<17 and day != "monday":
        price = 8*num 
    elif age>18 and age<64 and day != "monday":
        price = 12*num 
    else:
        price = 7*num 

    if day == "monday":
        price = price*0.9*num #10% discount

    print(f"you will be charged {price}$ , thank you {name}")

    choice = input("want to buy more? (y/n): ").lower()
    if choice != "y":
        break