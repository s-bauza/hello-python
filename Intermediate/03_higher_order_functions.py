
# Higher Order Functions

from functools import reduce


def sum_one(value):
    return value+1


def sum_five(value):
    return value+5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value+second_value)


print(sum_two_values_and_add_value(1, 2, sum_one))
print(sum_two_values_and_add_value(1, 2, sum_five))

# Closures


def sum_ten(original_value):
    def add(value):
        return original_value+10+value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

# Built-in Higher Order Functions

numbers = [1, 2, 3, 4, 5]

# Map


def multiply_by_two(number):
    return number*2


print(list(map(multiply_by_two, numbers)))
print(list(map(lambda number: number*2, numbers)))

# Filter


def is_even(number):
    return number % 2 == 0


print(list(filter(is_even, numbers)))
print(list(filter(lambda number: number > 2, numbers)))

# Reduce


def sum_two_values(first_value, second_value):
    return first_value+second_value


print(reduce(sum_two_values, numbers))
