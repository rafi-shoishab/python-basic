print("class 4")

num1, num2, num3 = map(int,input("enter 3 num: ").split())

if num1>num2:
    if num1>num3:
        print(f"{num1} largest")
    else:
        print(f"{num3} largest")

elif num2>num1:
    if num2>num3:
        print(f"{num2} largest")
    else:
        print(f"{num3} largest")