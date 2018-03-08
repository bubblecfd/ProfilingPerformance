# Timeit tutorial
# rriehle

from timeit import timeit as timer

my_repititions = 5000
my_range = 1000
my_lower_limit = my_range / 2

my_list = list(range(my_range))


def multiply_by_two(x):
    return x * 2


def greater_than_lower_limit(x):
    return x > my_lower_limit

# my_filtered_and_doubled_list = map(multiply_by_two, filter(greater_than_lower_limit, my_list))
# print(*my_filtered_and_doubled_list)
# Votes: 0
print(timer(
    'my_filtered_and_doubled_list = map(multiply_by_two, filter(greater_than_lower_limit, my_list))',
    globals=globals(),
    number=my_repititions
))

my_filtered_and_doubled_list_with_lambdas = map(lambda x: x * 2, filter(lambda x: x > my_lower_limit, my_list))
# print(*my_filtered_and_doubled_list_with_lambdas)
# Votes: 1
print(timer(
    'my_filtered_and_doubled_list_with_lambdas = map(lambda x: x * 2, filter(lambda x: x > my_lower_limit, my_list))',
    globals=globals(),
    number=my_repititions
))

# my_comprehension_with_functions = [multiply_by_two(x) for x in my_list if greater_than_lower_limit(x)]
# print(my_comprehension_with_functions)
# Votes: 0
print(timer(
    'my_comprehension_with_functions = [multiply_by_two(x) for x in my_list if greater_than_lower_limit(x)]',
    globals=globals(),
    number=my_repititions
))

# my_comprehension_without_functions = [x * 2 for x in my_list if x > my_lower_limit]
# print(my_comprehension_without_functions)
# Votes: 4
print(timer(
    'my_comprehension_without_functions = [x * 2 for x in my_list if x > my_lower_limit]',
    globals=globals(),
    number=my_repititions
))
