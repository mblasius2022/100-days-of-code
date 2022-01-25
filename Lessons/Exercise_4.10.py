"""
Your module description
# 4.10 Slicing a list
pets = ["cat","dog","ferret","hamster","gold fish","sloth","budgie"]
#first 3 from list
print(f"The first three itmes in Pets are {pets[:3]}")

#3 items middle of the list
print(f"Three items from the middle of the list are {pets[2:5]}")

#last 3 items of the list
print(f"Three items from the middle of the list are {pets[-3:]}")
"""

#4.11 Copying lists
my_pizzas = ['pepperoni','meat lovers', 'spicy veg trio']
my_friends_pizzas = my_pizzas[:]
my_pizzas.append("hawaiian")
my_friends_pizzas.append("margherita")
print(f"My favourite pizzas are {my_pizzas}")
print(f"My fiend's favourite pizzas are {my_friends_pizzas}")


#4.12More Looping through lists
print("\nMy Favourite Pizzas include:")
for pizza in my_pizzas:
    print(f" - {pizza}")
    
print("\n\nMy friends' favourite pizzas include:")
for pizza in my_friends_pizzas:
    print(f" - {pizza}")
    