# Define a tuple

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (27,1.70,"Satni","Bauzá","Hirschler")
my_other_tuple = (30,60,90)

print(my_tuple)
print(type(my_tuple))

# Accessing elements in a tuple and find

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(27))
print(my_tuple.index("Satni"))
print(my_tuple.index("Bauzá"))

#my_tuple[1] = 1.75 # TypeError: 'tuple' object does not support item assignment

# Concatenating tuples

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Sub-tuple

print(my_tuple[3:6]) # is like from 3 to 5, ==3 and 

# Convert a tuple to a list

my_tuple = list(my_tuple)

print(my_tuple)

my_tuple[4]="SBH"
my_tuple.insert(1,"Naranja")
my_tuple = tuple(my_tuple)

print(my_tuple)
print(type(my_tuple))

# Delete a tuple

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) # NameError: name 'my_tuple' is not defined 