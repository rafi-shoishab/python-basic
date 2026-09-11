# with open ("python.txt","w") as myfile:
#     myfile.write("this is my txt file....")

# with open ("python.txt","r") as p:
#     cntnt = p.read()
#     print(cntnt)

import os
# os.makedirs ("2026", exist_ok = True)
# os.makedirs ("2026/02", exist_ok = True)
# os.makedirs ("2026/01", exist_ok = True)
# os.makedirs ("2026/02/05", exist_ok = True)

# with open ("2026/02/05/sysb.png", "w") as mypng:
#     mypng.write("")

import csv
my_list = [
    ["id", "name", "cgpa"],
    [1, "soisob", 3.00],
    [2, "anim", 3.25]
]

# with open ("std.csv", "w", newline="") as mycsv:
#     writer = csv.writer(mycsv)
#     writer.writerows(my_list)

# with open ("std.csv", "r") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)

# import shutil

#  shutil.make_archive("class25","zip","02")

# import zipfile

# with zipfile.ZipFile("class25.zip","r") as zip_ref:
#     zip_ref.extractall("class")