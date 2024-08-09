 ### Lambdas ###
 
# Lambdas are a way to create anonymous functions in Python. They are defined using the lambda keyword, which has no meaning other than "we are defining a lambda function". Lambdas are useful when you need a short function that you will only use once. They are often used in conjunction with functions like map() and filter().

sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(3, 5))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(3, 7))

