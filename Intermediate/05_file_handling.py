# File handling

import xml
import csv
import json
import os

# .txt file

# read, write, overwrite if file exists
text_file = open("my_file.txt", "w+")  # read, write and overwrite

text_file.write(
    "Hello, World!\nThis is a new line.\nGeshin Impact is a great game.")

text_file.close()

text_file = open("my_file.txt", "r")

# print(text_file.read(5))
# print(text_file.read())

for line in text_file.readlines():
    print(line, end="")

text_file.close()

with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nThis is a new line.")

os.remove("my_file.txt")


# .json file

print("\n\n")

with open("my_file.json", "w+") as json_file_write:
    json_test = {
        "name": "Santiago",
        "age": 28,
        "city": "New York",
        "numbers": [1, 2, 3, 4, 5]
    }
    json.dump(json_test, json_file_write, indent=2)


with open("my_file.json", "r") as json_file_read:
    for line in json_file_read:
        print(line, end="")

print("\n\n")

json_dic = json.load(open("my_file.json"))
print(json_dic)
print(type(json_dic))
print(json_dic["name"])

os.remove("my_file.json")

# .csv file

with open("my_file.csv", "w+") as csv_file_write:
    csv_writer = csv.writer(csv_file_write)
    csv_writer.writerow(["name", "age", "city"])
    csv_writer.writerow(["Santiago", 28, "New York"])


with open("my_file.csv", 'r') as csv_file_read:
    for line in csv_file_read.readlines():
        print(line, end="") 

os.remove("my_file.csv")

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?