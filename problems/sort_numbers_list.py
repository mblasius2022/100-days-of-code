"""
2. Sort a list
Create a function in Python that accepts two parameters. The first will be a
list of numbers. The second parameter will be a string that can be one of the
following values: asc, desc, and none.

If the second parameter is "asc," then the function should return a list with
the numbers in ascending order. If it's "desc," then the list should be in
descending order, and if it's "none," it should return the original list
unaltered.
"""
from random import randint

numbers_list = []

def generate_numbers_list():
    x = 0
    while x < 10:
        number = randint(1,100)
        if number not in numbers_list:
            numbers_list.append(number)
            x += 1


def sort_list(numbers, sort):
    message = "\nnumbers sorted in "
    if sort == 'asc':
        numbers_list.sort()
        message += "ascending order:\n\t"
    elif sort == 'desc':
        numbers_list.sort(reverse = True)
        message += "descending order:\n\t"
    else:
        message += "original order:\n\t"

    print(f"{message} {numbers_list}")


generate_numbers_list()
sort_list(numbers_list, '')
sort_list(numbers_list, 'asc')
sort_list(numbers_list, 'desc')


