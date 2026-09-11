# conditional statement
print("class 2, 3")

mark = int(input("enter ur mark: "))

if mark>100:
    print("invalid input")
elif mark>=80:
    print("A+")
elif mark>=70:
    print("A")
elif mark>=60:
    print("A-")
elif mark>=50:
    print("B")
elif mark>=40:
    print("C")
elif mark>=33:
    print("pass")
else:
    print("Sorry! Failed")