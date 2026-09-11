print("class 4")

num1, num2 = map(int,input("enter 2 num: ").split())

sign = input("enter operators + - * /: ")

if sign == "+":
    print(f"Add: {num1+num2}")
elif sign == "-":
    print(f"sub: {num1-num2}")
elif sign == "*":
    print(f"mul : {num1*num2}")
elif sign == "/":
    print(f"div {num1/num2}")
else:
    print("invalid")