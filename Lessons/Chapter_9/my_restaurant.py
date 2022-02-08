"""
Builds a restaurant
"""
from restaurants import *


new_ice_cream_stand = IceCreamStand('Gelato')
new_ice_cream_stand.ice_cream_flavours = ['vanilla', 'chocalate', 'strawberry', 'matcha tea', 'bubble gum']
print(new_ice_cream_stand.describe_restaurant())
new_ice_cream_stand.describe_flavours()

x = 0
while x < 10:
    new_ice_cream_stand.increment_number_served(1)
    print(f"\nNow served {new_ice_cream_stand.number_served} customers")
    x += 1
