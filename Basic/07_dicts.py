
# Dictionaries

# Define a dictionary

my_dict = dict()
my_other_dict = {}

my_other_dict = {
    'name': 'Santi',
    'last name': 'Bauzá',
    'age': 27,
    1: 'Python'
}

my_dict = {
    'name': 'Santi',
    'last name': 'Bauzá',
    'age': 27,
    'Lenguages': {'C','C++','Python','Java'},
    1: 1.70
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Find a value in a dictionary

print(my_dict[1])
print(my_other_dict['name'])

print('Santi' in my_dict)
print('last name' in my_dict)

# Insert

my_dict['city'] = 'Madrid'
print(my_dict)

# Remove

del my_dict['city']
print(my_dict)

# Other operations

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['name', 'last name', 'age']

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict) 
my_new_dict = dict.fromkeys(('Santi', 'Bauzá', 27))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, 'Santi')
print((my_new_dict))    

my_value = my_new_dict.values()
print(type(my_value))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))