# Loops

# While loop

my_condition = 0

while my_condition < 5:
    print('The condition is:', my_condition)
    my_condition += 1
else:
    print('The condition is bigger than 5')
    
print('The execution continues...')

while my_condition < 10:
    my_condition += 1
    if my_condition == 7:
        print('The condition stopped')
        break
    print('The condition is:', my_condition)
    
# For loop

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print('The element is:', element)
    
my_tuple = (27, 1.68, 'Santi', 'Bauzá')

for element in my_tuple:
    print('The element is:', element)
    
my_set = {27, 1.68, 'Santi', 'Bauzá'}

for element in my_set:
    print('The element is:', element)

my_dict = {'yellow': 'banana', 'red': 'apple', 'green': 'pear'}
 
for key in my_dict:
    print('The key is:', key)
    if key == 'red':
        break
else:
    print('The dictionary loop finished')

for key in my_dict:
    print('The key is:', key)
    if key == 'red':
        continue
    print('Executing the continue block')
else:
    print('The dictionary loop finished')