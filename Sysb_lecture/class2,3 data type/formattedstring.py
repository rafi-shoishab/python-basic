# practice example
print("class 2, 3")

first_name, last_name = map(str, input("ur 1st name and last name separeted by space: ").split())
contact = int(input("ur mobile: +88"))
mail = input("ur email: ")
street, postoffice, district = map(str, input("enter ur street, thana, district separated by space: ").split())
postcode = int(input("Postcode: "))
address = street+ " , " + postoffice + " , " + district + " , "

print("full Name:", first_name, last_name)
print("email: ", mail) 
print("mobile: ", contact) 
print(f"address: {address} {postcode}") 
