# 2. Create a simple ATM simulation (check balance, withdraw, deposit).

balance = 1500
choice = 0
while choice != 4:
    print("===ATM Menu===")
    print("1. check balance")
    print("2. withdraw")
    print("3. deposit")
    print("4. exit")
    
    choice = int(input("input ur choice 1-3 : "))

    if choice == 1:
        print ("ur current balance is: ", balance)

    elif choice == 2:
        withdraw = float(input("enter withdraw amount: "))
        if withdraw>0 and withdraw<=balance:
            print("withdraw successfull!")
            balance = balance - withdraw
            print("new balance is: ", balance)
        else:
            print("withdraw not possible!")

    elif choice == 3:
        diposit = float(input("enter deposite amount: "))
        if diposit>0:
            print("diposit succesful!")
            balance = balance + diposit
            print("new balance is: ", balance)
        else:
            print("insufficient amount")

    else:
        print("invalid choice!")
