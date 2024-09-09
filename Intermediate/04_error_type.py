# Error Types

import math
from math import pi

# Syntax Error

# print "Hello, World!" # Syntax Error
print("Hello, World!")

# Name Error
language = "Spanish"  # Coment this line to see the error
print(language)

# Index Error

my_list = [1, 2, 3, 4, 5]

print(my_list[0])
print(my_list[-1])
# print(my_list[5]) # Index Error

# Module Not Found Error
# import maths # Uncomment this line to see the error

# Attribute Error

# print(math.PI) # Uncomment this line to see the error
print(math.pi)

# KeyError
my_dict = {"name": "Santiago", "age": 28}
# print(my_dict["Name"]) # Uncomment this line to see the error
print(my_dict["name"])

# Type Error
# print(my_list["0"]) # Uncomment this line to see the error
print(my_list[0])
print(my_list[False])

# Import error
# from math import PI # Uncomment this line to see the error
print(pi)

# Value Error
# my_int = int("10 years") # Uncomment this line to see the error
my_int = int("10")
print(type(my_int))

# Zero Division Error
# print(4/0) # Uncomment this line to see the error
print(0/4)
