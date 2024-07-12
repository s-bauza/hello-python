# List Comprehension

my_original_list = [0, 1, 2, 3, 4, 5]
print(my_original_list)

my_range = range(6)
print(list(my_range))

my_list = [i for i in range(6)]
print(my_list)

my_list = [i * 2 for i in range(6)]
print(my_list)

my_list = [i * i for i in range(6) if i < 3]
print(my_list)

def sum_five(value):
    return value + 5    

my_list = [sum_five(i) for i in range(6)]
print(my_list)