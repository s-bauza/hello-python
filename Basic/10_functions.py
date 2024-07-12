
# Functions

# Define a function

def my_function():
  print("Hello from a function")
  
my_function()
my_function()
my_function()

# Function Arguments

def sum(first_value: int , second_value):
  print(first_value + second_value)
  
sum(2, 3)
sum(54667,71231)
sum('5','7')
sum(1.5,2.4)

# Function return

def sum_with_return(first_value, second_value):
  return first_value + second_value

print(sum_with_return(2, 3))    

my_result = sum_with_return(2.6, 3.4)
print(my_result)
my_result = sum_with_return(54667,71231)
print(my_result)

# Function with keyword arguments

def print_name(name,surname):
  print(name + " " + surname)
  
print_name(name="Santi",surname="Bauzá")


# Function with default parameter

def print_name_with_default(name,surname,alais="Tigretoon"):
  print(name + " " + surname + ' ' + alais)

print_name_with_default(name="Santi",surname="Bauzá")
print_name_with_default(name="Santi",surname="Bauzá",alais="Cordico") 

# Functions with arbitrary arguments

def print_upper_text(*texts):
  print(texts)  
  for text in texts:
    print(text.upper())

print_upper_text("Hello", "World", "Python")
print_upper_text("Hello")