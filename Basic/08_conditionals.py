
#Conditionals

# IF

my_condition = True

if my_condition:
    print('Entered the IF block')

my_condition = 5 * 5 

if my_condition == 25:
    print('Entered the IF block')
    
# IF, ELSE, ELSE

if my_condition > 10 and my_condition < 20:
    print('Entered the IF block')
elif my_condition == 25:
    print('Entered the ELIF block')
else:
    print('Entered the ELSE block')
    
print('The ejecution continues...')

my_string = ''

if not my_string:
    print('The string is empty')

if my_string == 'This is a string':
    print('The string is not empty')