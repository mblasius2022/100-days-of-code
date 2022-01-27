
"""
Chapter Four Exercises - Working with lists

# 4.1
pizzas = ['pepperoni','meat lovers', 'spicy veg trio']

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I Like {pizza} pizza")
print("I really like pizza")


# 4.2
pets = ["cat","dog","ferret","hamster"]
for pet in pets:
    print(pet)
    
for pet in pets:
    print (f"A {pet} would make a great pet")
print("Any of these would make a great pet")


#Numerical lists


#4.3 count to 20
for number in range (1,21):
    print(number)
    
#4.4 one million
for number in range(1,1000001):
    print(number)
 
#4.5 summing a million
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))


#4.6  odd numbers between 1 and 20
for number in range(1,21,2):
    print(number)


#4.7 multiples of threes
threes = [value * 3 for value in range (1,31)]
print(threes)
for three in threes:
    print(three)
 
print("\nprinting multiples of 3 for numbers between 1 and 30 inclusive:")   
for three in range(1,31):
    print (three*3)
    


#4.8 and 4.9 cubes
cubes = [value **3 for value in range(1,11)]
print(f"the min of cubes = {min(cubes)} and the max = {max(cubes)}")
max(cubes)
print(cubes)
for cube in cubes:
    print(cube)



# 4.10 Slicing a list
pets = ["cat","dog","ferret","hamster","gold fish","sloth","budgie"]
#first 3 from list
print(f"The first three itmes in Pets are {pets[:3]}")

#3 items middle of the list
print(f"Three items from the middle of the list are {pets[2:5]}")

#last 3 items of the list
print(f"Three items from the middle of the list are {pets[-3:]}")


# 4.11 Copying lists
my_pizzas = ['pepperoni','meat lovers', 'spicy veg trio']
my_friends_pizzas = my_pizzas[:]
my_pizzas.append("hawaiian")
my_friends_pizzas.append("margherita")
print(f"My favourite pizzas are {my_pizzas}")
print(f"My fiend's favourite pizzas are {my_friends_pizzas}")


# 4.12More Looping through lists
print("\nMy Favourite Pizzas include:")
for pizza in my_pizzas:
    print(f" - {pizza}")
    
print("\n\nMy friends' favourite pizzas include:")
for pizza in my_friends_pizzas:
    print(f" - {pizza}")

"""   

# TUPLES

#4.13 Buffet
buffet_foods = ('Tacos', 'Burrito','Chips and Dip','Enchilada','Salad')
print("Original Buffet Menu Items:")
for food in buffet_foods:
    print(food)

# modify tuple and generate error
#buffet_foods[2] = 'Nachos'


buffet_foods = ('Tacos', 'Burrito','Nachos','Quesadilla','Salad')
print("\nNew Buffet Menu Items:")
for food in buffet_foods:
    print(food)