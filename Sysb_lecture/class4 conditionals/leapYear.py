# 4. Check if a year is a leap year.

year = int(input("enter the year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print ("leap year")
else:
    print("not leap year")