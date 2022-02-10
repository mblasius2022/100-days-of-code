"""
3. Convert a decimal number into binary
Write a function in Python that accepts a decimal number and returns the
equivalent binary number. To make this simple, the decimal number will always
be less than 1,024, so the binary number returned will always be less than ten
digits long.
"""
def decimal_to_binary(number):
    return bin(number).replace('0b','')

x = 1
while x <= 10:
    binary_representation = decimal_to_binary(x)
    print(f"{x} in binary is {binary_representation}")
    x += 1