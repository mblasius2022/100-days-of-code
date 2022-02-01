"""
Chapter 7 - User Input and While Loops
"""
#message = input("Tell me something and I will repeat it back to you: ")
#print(message)

#name = input("Enter your name: ")
#print(f"\nHello {name}!")

#7.1
# prompt = "Welcome to XYZ Rentals"
# prompt += "\nWhat brand of car would you like? "
# car_brand = input(prompt)
# print(f"Let me see if I can find you a {car_brand.title()}")

#7.2
# prompt = "Welcome to Pasta Paradise\nHow many people in your group? "
# group_size = input(prompt)
# group_size = int(group_size)
# if group_size < 8:
#     print("\n\tWe have a table ready for you")
# else:
#     print("\n\tI'm sorry but you will have to wait a few minutes for a table")

#7.3
# number = input("please enter a whole number: ")
# number = int(number)
# if number % 10 == 0:
#     status = 'is'
# else:
#     status = 'is not'
# print(f"{number} {status} a multiple of 10")

#7.4
# prompt = "What toppings would you like on your pizza?\nEnter 'quit' when done."
# toppings_list = []
# active = True
# while active == True:
#     toppings = input(prompt)
#     if toppings == 'quit':
#         active = False
#     else:
#         toppings_list.append(toppings)

# for topping in toppings_list:
#     print(f"Adding {topping}")

# #7.5
# active = True
# while active == True:
#     age = input("Please enter your age.\nJust hit enter to exit\t")
#     if age == '':
#         active = False
#         print("\n\tThank you for coming")
#     else:
#         age = int(age)
#         if age < 3:
#             price = 'Free'
#         elif age >= 3 and age < 12:
#             price = '$10.00'
#         else:
#             price = '$15.00'

#         print(f"\n\tYour ticket price is {price}\n")

#7.6
# while True:
#     age = input("Please enter your age.\nJust hit enter to exit\t")
#     if age == '':
#         print("\n\tHave a great day")
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             price = 'Free'
#         elif age >= 3 and age < 12:
#             price = '$10.00'
#         else:
#             price = '$15.00'

#         print(f"\n\tYour ticket price is {price}\n")

#7.7 - Infinite Loop
# x = 1
# while x < 5:
#     print(x)
#     #x += 1
