pswrd = " "
user = " "
while (user != "admin" ) or (pswrd != "123"):
    user = input("enter user name: ")
    pswrd = input("enter ur 3 digit password: ")
    if (user != "admin") or (pswrd != "123"):
        print ("try again")

print("log in successfull") 