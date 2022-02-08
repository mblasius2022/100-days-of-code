"""
Simple dice program
"""
from random import randint

class Dice:
    """ A simple attempt to represent a dice """

    def __init__(self, sides=6):
        """ Initialize attributes of dice """
        self.sides = sides

    def roll_dice(self):
        spots = randint(1,self.sides)
        print(f"You rolled a {spots} on a {self.sides} sided dice")

x = 1
while x < 10:
    my_6_sided_dice = Dice()
    my_6_sided_dice.roll_dice()
    x += 1

x = 1
while x < 10:
    my_10_sided_dice = Dice(10)
    my_10_sided_dice.roll_dice()
    x += 1


x = 1
while x < 10:
    my_6_sided_dice = Dice(20)
    my_6_sided_dice.roll_dice()
    x += 1