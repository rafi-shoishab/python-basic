# 2. Create a simple ATM simulation (check balance, withdraw, deposit).

balance = 1500

print("===ATM Menu===")
print("1. check balance")
print("2. withdraw")
print("3. deposit")
print("4. exit")

while True:
    choice = int(input("input ur choice 1-4 : "))

    if choice == 1:
        print ("ur balance is: ", balance)

    elif choice == 2:
        amount = float(input("enter amount: "))
        if amount>0 and amount<balance:
            balance = balance - amount
            print("withdraw successfull!")
            print("remaining balance: ", balance)
        else:
            print("withdraw not possible!")

    elif choice == 3:
        diposit = float(input("enter deposite amount: "))
        if diposit>0:
            balance = balance + diposit
            print("diposit succesful!")
            print("new balance: ", balance)
        else:
            print("invalid diposit")
    
    elif choice == 4:
            print("Thanks. Bye!")
            break
    else:
        print("invalid request!")
