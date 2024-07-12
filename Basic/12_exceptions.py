# Exceptions

numberOne = 5
numberTwo = 1
numberTwo = '1'

# Exception base: try, except

try:
    print(numberOne + numberTwo)   
    print('This line will not be executed')
except:
    print('An exception occurred')
    
# A flow exception block

try:
    print(numberOne + numberTwo)   
    print('This line will not be executed')
except:
    print('An exception occurred')
else:
    print('The exception block continues')
finally:
    print('This block will always be executed')
    
# Specific exception block

try:
    print(numberOne + numberTwo)   
    print('This line will not be executed')
except ValueError:
    print('A ValueError occurred')  
except TypeError:
    print('A TypeError occurred')
    
# Capture the exception object

try:
    print(numberOne + numberTwo)   
    print('This line will not be executed')
except TypeError as error:
    print('An exception occurred:', error)
except Exception as my_random_error_object:
    print('An exception occurred:', my_random_error_object)