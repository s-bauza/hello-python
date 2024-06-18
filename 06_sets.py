# Definding Sets

my_set = set()
my_other_set = {}

print(my_set)
print(type(my_set))

my_other_set = {'apple', 'banana', 'cherry','orange'}
print(type(my_other_set))

print(len(my_other_set))

# Inserting elements in a set

my_other_set.add('orange')

print(my_other_set) # A set does not allow duplicates

# Funding elements in a set

print('apple' in my_other_set)
print('grape' in my_other_set)

# Remove

my_other_set.remove('banana')
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set
# print(my_other_set) # NameError: name 'my_other_set' is not defined   

# Transforming

my_set = {'a', 'b', 'c'}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'C', 'Java', 'Python'}

# Other operations

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_other_set).union(my_set).union({'C++'}))
print(my_new_set.difference(my_set))
