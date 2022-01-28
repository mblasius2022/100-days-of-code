"""
CHAPTER 5 EXERCISES - IF STATEMENTS
"""
"""
#5.1 Conditionl tests
car = 'subaru'
print("Is car == subaru? I predict True")
print(car=='subaru')

print("Is car == audi? I predict False")
print(car=='audi')

#test for equality with string
print("Is car == SUBARU")
print(car=='SUBARU')
print("car != SUBARU")
print(car != 'SUBARU')
print("is car.lower == 'subaru")
print(car.lower()=='subaru')

x,y = 18,21
print(f"x=y is {x==y}")
print(f"x>y is {x>y}")
print(f"x<y is {x<y}")
print(f"x!=y is {x!=y}")
print(f"x times y = 35 is {x*y==35}")

a=19
print(f"you can drive,vote and drink is {a>x and a>=y}")
print(f"you can drive,vote and drink is {a>x or a>=y}")

fruits = ['apple', 'orange', 'lemon', 'grape', 'watermelon']
if 'tomato' not in fruits:
    print(f"tomato is not in your list of fruits")

fruits.append('tomato')
print(f"tomato is a fruit = {'tomato' in fruits}")

alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points")
if alien_color == 'red':
    print("You earned 5 points")


#5.4 alien colors 2
alien_color = 'red'
if alien_color == 'green':
    print(f"You just earned 5 points for shooting a {alien_color} alien")
else:
    print(f"You just earned 10 points for shooting a {alien_color} alien")


#5.5 alien colors 3
alien_color = 'red'
if alien_color == 'green':
    print(f"You just earned 5 points for shooting a {alien_color} alien")
elif alien_color == 'yellow':
    print(f"You just earned 10 points for shooting a {alien_color} alien")
elif alien_color == 'red':
    print(f"You just earned 10 points for shooting a {alien_color} alien")
else:
    print("You didn't earn any points")


alien_color = 'yellow'
if alien_color == 'green':
    print(f"You just earned 5 points for shooting a {alien_color} alien")
elif alien_color == 'yellow':
    print(f"You just earned 10 points for shooting a {alien_color} alien")
elif alien_color == 'red':
    print(f"You just earned 15 points for shooting a {alien_color} alien")
else:
    print("You didn't earn any points")


alien_color = 'green'
if alien_color == 'green':
    print(f"You just earned 5 points for shooting a {alien_color} alien")
elif alien_color == 'yellow':
    print(f"You just earned 10 points for shooting a {alien_color} alien")
elif alien_color == 'red':
    print(f"You just earned 10 points for shooting a {alien_color} alien")
else:
    print("You didn't earn any points")
"""
"""
#5.6 Stages of life
age = 3
if age < 2:
    print("you are a baby")
elif age >= 2 and age < 4:
    print("you are a toddler")
elif age >=4 and age < 13:
    print("you are a kid")
elif age >=13 and age <20:
    print("you are a teenager")
elif age >= 20 and age < 65:
    print("you are an adult")
elif age >= 65:
    print("you are an elder")

age = 3
if age < 2:
    status = 'baby'
elif age >= 2 and age < 4:
    status = 'toddler'
elif age >=4 and age < 13:
    status = 'kid'
elif age >=13 and age <20:
    status = 'teenager'
elif age >= 20 and age < 65:
    status = 'adult'
elif age >= 65:
    status = 'elder'
print(f"You are a {status}")


#5.7 favourite fruits
favourite_fruits = ['apple', 'banana', 'fig']
fruit = 'apple'
if 'pomegranite' in favourite_fruits:
    print(f"Really ... {fruit} is your favourite fruit")
if 'fig' in favourite_fruits:
    print(f"Really ... {fruit} is your favourite fruit")
if 'tomato' in favourite_fruits:
    print(f"Really ... {fruit} is your favourite fruit")
if 'apricot' in favourite_fruits:
    print(f"Really ... {fruit} is your favourite fruit")

#5.8
usernames = ('admin','bob', 'jane', 'peter', 'paul', 'mary')
for user in usernames:
    if user =='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Welcome {user} ... have a great day!")

#5.9
usernames = []
if usernames:
    print(usernames)
else:
    print("we need some users!")


#5.10
current_users = ('admin','bob', 'jane', 'peter', 'paul', 'mary')
new_users = ('BOB', 'jane', 'troy', 'barnaby')
for user in new_users:
    if user.lower() in current_users:
        print (f"username {user} already exists; please choose a new name")
    else:
         print(f"username {user} is available")
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f"{number}th"
)