"""
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number. 13 is a divisor of 26 because 26 / 13 has no
remainder.
"""
n = int(input("enter a number: "))
numbers = [range(1,n)]

divisors = []
x = 1
while x <= n:
    if n % x == 0:
        divisors.append(x)
    x+=1

print(f"the numbers that divide into {n} are {divisors}")
