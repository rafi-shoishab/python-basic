"""Number Range Classifier
Input a number and classify it as:
Small (0-10)
Medium (11-100)
Large (101-1000)
Invalid (negative or above 1000)"""

num = int(input("inout a number: "))
if num<=1000 and num>=101:
    print("its a large number")
elif num<=100 and num>=11:
    print("its a medium number")
elif num<=10 and num>=0:
    print("its a small number")
else:
    print("invalid number")