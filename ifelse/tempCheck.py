"""Body Temperature Checker
Input a temperature and print:
"Hypothermia" if below 35°C
"Normal" if 35-37.5°C"""

temp = float(input("enter ur temperature ('C): "))

if temp<=37.5 and temp>=35:
    print("Normal Temparature")
elif temp<35:
    print("Hypothermia")
else:
    print("Fever")
