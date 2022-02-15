"""
and write a program that prints out all the elements of the list that are less
than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from
the original list a that are smaller than that number given by the user.
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

def get_numbers_from_list(n):
    for number in numbers:
        if number < n:
            print(number)
            new_list.append(number)

    print(new_list)

n = int(input("enter a number: "))
get_numbers_from_list(n)

# combine challenges 1 and 2:
print( [ x for x in numbers if x<n ] )