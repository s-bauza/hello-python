# Classes

# Define a class

class MyEmptyClass:
    pass # empty class

print(MyEmptyClass)
print(MyEmptyClass()) 

# Class with constructor,  destructor, methods and  private and public attributes

class Person:
    def __init__(self, name, surname, alias='Without alias'):
        self.full_name = f'{name} {surname} ({alias})' # public attribute
        self._name = name # protected / private attribute
    
    def __del__(self):
        print("Destructor called")
    
    def get_name(self):
        return self._name
    
    def walk(self):
        print(f'{self._name} is walking')
        
person = Person('Santi', 'Bauzá')	

print(person.full_name)
print(person.get_name())
person.walk()

person2 = Person('Santi', 'Bauzá','Tigretoon')
print(person2.full_name)
print(person2.get_name())
person2.full_name = 'Santi Bauzá el más (grande de todos)'
print(person2.full_name)

person2.full_name = 666
print(person2.full_name)
print(person2.get_name())