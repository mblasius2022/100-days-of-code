"""Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. Print
out a message addressed to them that tells them the year that they will turn
100 years old.

Extras:

Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message. (Hint: order of
operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint:
the string "\n is the same as pressing the ENTER button)
"""

# get current year
from datetime import date


def get_details():
    """ # Get name and age
        Calculate year that user will turn 100
        """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    year = date.today().year + (100-int(age))
    print(f"Hi {name} ... you will turn 100 in the year {year}")
    number = int(input("Enter a Number: "))
    print(f"Hi {name} ... you will turn 100 in the year {year}" * number)

    print(f"Hi {name} ... you will turn 100 in the year {year}\n" * number)




get_details()
