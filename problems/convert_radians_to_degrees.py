"""
1. Convert radians into degrees
Write a function in Python that accepts one numeric parameter. This parameter
will be the measure of an angle in radians. The function should convert the
radians into degrees and then return that value.
"""
import math

def convert_radians():
    """ try and convert the provided number of rads to degrees"""
    rad = input("Enter number of radians to conver: ")
    try:
        pi = 3.14159265358979323846264338327950288419716939937510
        rad = int(rad)
        degrees = (rad * 180)/pi
        print(f"{rad} radians converts to approx {round(degrees,2)} degrees")

        print(f"Using built in math function {round(math.degrees(rad),2)}")

    except ValueError:
        print("You didn't enter a number")


convert_radians()
