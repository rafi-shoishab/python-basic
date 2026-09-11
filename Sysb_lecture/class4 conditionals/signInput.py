print("class 4")

num1, num2 = map(int,input("enter 2 num: ").split())

sign = input("enter + to add, - to sub: ")

if sign == "+":
    print(num1+num2)
elif sign == "-":
    print(num1-num2)