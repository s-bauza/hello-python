# Regular Expressions

import re

# match

my_string = "The rain in Spain"
my_other_string = "The sun in Spain"

match = re.match("The rain", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("The sun", my_other_string)
# if not(match==None):
# if match != None:
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("in Spain", my_other_string))

# search

search = re.search("rain", my_string)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("in", my_string)
print(findall)

# split

print(re.split("in", my_string))

# sub

print(re.sub("[T|t]he", "THE", my_string))
print(re.sub("in Spain", "spain", my_string))

# Regular Expressions Patterns

# To learn and validate regular expressions https://regex101.com

pattern = r"[tT]he"
print(re.findall(pattern,my_string))

pattern = r"[tT]he|Spain"
print(re.findall(pattern,my_string))

pattern = r"[0-9]"
print(re.findall(pattern,my_string))
print(re.search(pattern,my_string))

pattern = r"\d"
print(re.findall(pattern,my_string))

pattern = r"\D"
print(re.findall(pattern,my_string))

pattern = r"[T].*"
print(re.findall(pattern,my_string))

email = "santiago.bauza@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "santiago.bauza@gmail.com.es"
print(re.findall(pattern,email))

