# Lists

# Defining a list

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [1, 1, 2, 3, 4, 5]

print(my_list)
print(len(my_list))

my_other_list = [27, 1.70, "Bauzá", "Santiago"]

print(type(my_list))
print(type(my_other_list))

# Accessing elements in a list and fundings

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count(27))
# print(my_other_list[10]) # IndexError: list index out of range

print(my_other_list.index("Bauzá"))

age, height, surname, name = my_other_list
print(name)

name, height, age, surname = my_other_list[3], my_other_list[1], my_other_list[0], my_other_list[2]
print(name)

# Concatenating lists

print(my_list + my_other_list)
# print(my_list - my_other_list) # TypeError: unsupported operand type(s) for -: 'list' and 'list'

# creating, inserting, updating and deleting elements in a list

my_other_list.append("Cordico")
print(my_other_list)

my_other_list.insert(1, "Blanco")
print(my_other_list)

my_other_list[1] = "Naranja"
print(my_other_list)

my_other_list.remove("Naranja")
print(my_other_list)

my_list.remove(1)
print(my_list)

my_list.pop()
print(my_list)

my_pop_element = my_list.pop(2) # pop(x) returns the element that was removed and x is the index of the element to remove 
print(my_pop_element)
print(my_list)

del my_list[2]# is the same as my_list.pop(2)
print(my_list)

#List operations

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

#Sublists

print(my_new_list[1:3])

#Changing the type of a list

my_list = "Hello World"
print(my_list)
print(type(my_list))

