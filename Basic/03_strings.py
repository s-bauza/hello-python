#Strings

my_string = "My string"
my_other_string = 'My other string'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "This is a string\nwith a new line"
print(my_new_line_string)

my_tab_string = "This is a string\twith a tab"
print(my_tab_string)

my_scaped_string = "This is a string with a backslash \\"
print(my_scaped_string)

#Format 
name, age = "Santi", 27
print("My name is %s and I am %d years old" % ("Santi", 27))
print("My name is {} and I am {} years old".format("Santi", 27))
print("My name is "+name+" and I am "+str(age)+" years old")
print(f"My name is {name} and I am {age} years old")

#Get a character from a string
lenguage = "Python"
a, b, c, d, e, f = lenguage
print(a)
print(b)


#Slice a string
print(lenguage[0])
print(lenguage[-1])
print(lenguage[1:3])#From 1 to 3
print(lenguage[1:])
print(lenguage[0:6:2])

#Reverse a string
print(lenguage[::-1])


#Lenguage functions
print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.lower())
print(lenguage.count("t"))
print(lenguage.isdigit())
print("123".isdigit())
print(lenguage.lower().isupper())
print(lenguage.startswith("Py"))
print("Py"=="Py")