try:
    with open ("file_name.txt", "r") as err:
        cntnt = err.read()
        print(cntnt)
except Exception as exp:
    print("error: {exp}")
finally:
    print("try again")