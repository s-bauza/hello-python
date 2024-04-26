# Variables

my_string_varaible = "My String variable"
print(my_string_varaible)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))#<class 'str'>

my_bool_variable = True
print(my_bool_variable)

print(my_string_varaible,my_int_variable,my_bool_variable)
print("This is value of: ",my_bool_variable)

# Some system functions
print(len(my_string_varaible))

# Variables in only one line
name, surname = "Santiago", "Bauzá"
print(name,surname)
print("My name is:", name, "and my surname is:", surname)

# Input
'''
first_name=input("What is your first name? ")
age=input("How old are you? ")
print(first_name,age)
'''

# Change the type of a variable
name = 123
print(name)

# Forcing the type of a variable
address: str = "My address"
address = 123
address = True
address = 1.5
print(type(address))



