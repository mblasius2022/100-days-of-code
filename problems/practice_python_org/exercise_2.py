"""
The exercise comes first (with a few extras if you want the extra challenge
or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that
to the user. If not, print a different appropriate message.
"""

def get_remainder(num, check=0):
    if check == 0:
        if num % 4 == 0:
            print(f"{num} is even and a multiple of 4")
        elif num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    else:
        if num % check == 0:
            print(f"{check} divides evenly into {num}")
        else:
            remainder = num%check
            print(f"The remainder of {num} divided by {check} is {remainder}")

num = int(input("enter a number: "))
check = int(input(f"enter a number to divide {num} by: "))
get_remainder(num, check)