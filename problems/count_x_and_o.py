"""6. Are the Xs equal to the Os?
Create a Python function that accepts a string. This function should count the
number of Xs and the number of Os in the string. It should then return a
boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True. If
the count isn't the same, it should return False. If there are no Xs or Os in
the string, it should also return True because 0 equals 0. The string can
contain any type and number of characters.
"""

def count_x_and_o(word):
    """ get and compare number of x's and o's in a string"""
    characters = list(word)
    x_count = 0
    o_count = 0
    for char in characters:
        if char == 'x' or char == 'X':
            x_count += 1
        elif char == 'o' or char == 'O':
            o_count += 1

    if o_count == x_count:
        return True
    else:
        return False

print(f"predict True: {count_x_and_o('better')}")

print(f"predict False: {count_x_and_o('Zebra')}")

print(f"predict True: {count_x_and_o('zo')}")

print(f"predict False: {count_x_and_o('zoo')}")
