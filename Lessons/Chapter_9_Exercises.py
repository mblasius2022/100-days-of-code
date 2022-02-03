#9.1 Restuarants

# class Restaurant:
#     """ A simple attempt to represent a restaurant """
#     def __init__(self, name, cuisine):
#         """ Initialize atrributes of restaurant """
#         self.name = name.title()
#         self.cuisine = cuisine.title()


#     def describe_restaurant(self):
#         """ return a neatly formatted opening message """
#         opening_message = f"{self.name} is now open and serving great {self.cuisine} food"
#         return opening_message


# new_restaurant = Restaurant('Ali Baba','Turkish')
# print(new_restaurant.name)
# print(new_restaurant.cuisine)
# print(f"\n{new_restaurant.describe_restaurant()}")

# #9.2 three restaurants
# new_italian_restaurant = Restaurant('Marco Polo', 'Italian')
# new_mexican_restaurant = Restaurant('Pancho Villa', 'mexican')
# new_asian_restaurant = Restaurant('Golden Wok','Asian')
# print(f"\n{new_italian_restaurant.describe_restaurant()}")
# print(f"\n{new_mexican_restaurant.describe_restaurant()}")
# print(f"\n{new_asian_restaurant.describe_restaurant()}")

#9.3
# class User:
#     """ A simple user class """
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age


#     def describe_user(self):
#         message = f"Hello {self.first_name.title()} {self.last_name.title()},"
#         message += f"\nI believe you are {self.age} years old"
#         return message

# new_user = User('Sponge Bob','Squarepants',7)
# print(new_user.describe_user())

#9.4
# class Restaurant:
#     """ A simple attempt to represent a restaurant """
#     def __init__(self, name, cuisine, number_served=0):
#         """ Initialize atrributes of restaurant """
#         self.name = name.title()
#         self.cuisine = cuisine.title()
#         self.number_served = number_served


#     def describe_restaurant(self):
#         """ return a neatly formatted opening message """
#         opening_message = f"\n{self.name} is now open " + \
#                           f"\nServing great {self.cuisine} food " + \
#                           f"to {self.number_served} customers and counting"
#         return opening_message


#     def set_number_served(self, number_served):
#         """Add a given amount to the number of people served"""
#         self.number_served = number_served


#     def increment_number_served(self, number_served):
#         """ increment the number of people served by a given amount"""
#         self.number_served += number_served


# new_italian_restaurant = Restaurant('Marco Polo', 'Italian')
# print(new_italian_restaurant.describe_restaurant())

# new_italian_restaurant.set_number_served(30)
# print(new_italian_restaurant.describe_restaurant())

# x = 0
# while x < 6:
#     increase_number_served = new_italian_restaurant.number_served * 2
#     new_italian_restaurant.increment_number_served(increase_number_served)
#     print(new_italian_restaurant.describe_restaurant())
#     x +=1

#9.5 Login attempts
# class User:
#     """ A simple user class """
#     def __init__(self, user_name, first_name, last_name, login_attempts=0):
#         self.user_name = user_name
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = login_attempts


#     def describe_user(self):
#         description =   f"Username:\t{self.user_name}" + \
#                         f"\nFirst Name:\t{self.first_name.title()}" + \
#                         f"\nLast Name:\t{self.last_name.title()}," + \
#                         f"\nLogin Attempts:\t{self.login_attempts}"
#         return description


#     def reset_login_attempts(self):
#         self.login_attempts = 0


#     def increment_login_attempts(self):
#         self.login_attempts += 1


# new_user = User('spongebob@squarepants.com','Sponge Bob','Squarepants')
# print(new_user.describe_user())
# print("\n\n")

# x = 0
# while True:
#     if x < 10:
#         new_user.increment_login_attempts()
#         print(f"Login Attempts: {new_user.login_attempts}")
#     else:
#         print("Login Attempts Exceeded. Wait 10 minutes before trying again")
#         break
#     x += 1


# new_user.reset_login_attempts()
# print(f"Login attempts have been reset to {new_user.login_attempts}")

#9.6
class Restaurant:
    """ A simple attempt to represent a restaurant """
    def __init__(self, name, cuisine):
        """ Initialize atrributes of restaurant """
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.number_served = 50


    def describe_restaurant(self):
        """ return a neatly formatted opening message """
        opening_message = f"\n{self.name} is now open " + \
                          f"\nServing great {self.cuisine} " + \
                          f"to {self.number_served} customers and counting"
        return opening_message


    def set_number_served(self, number_served):
        """Add a given amount to the number of people served"""
        self.number_served = number_served


    def increment_number_served(self, additional_number_served):
        """ increment the number of people served by a given amount"""
        self.number_served += additional_number_served


class IceCreamStand(Restaurant):
    """ Ice cream stands are a special type of restaurant"""

    def __init__(self, name, cuisine='Ice Cream'):
        """
        Initialize atrributes of parent restaurant
        and then initialize attributes specific to Ice Creaam Stand
        """
        super().__init__(name, cuisine)
        self.ice_cream_flavours = []


    def describe_flavours(self):
        """ returns formatted list of flavours"""
        print("\nWe have the following flavors available:")
        for flavour in self.flavours:
            print(f"\t- {flavour.title()}")


new_ice_cream_stand = IceCreamStand('Gelato')
new_ice_cream_stand.flavours = ['vanilla', 'chocalate', 'strawberry', 'matcha tea', 'bubble gum']
print(new_ice_cream_stand.describe_restaurant())
new_ice_cream_stand.describe_flavours()

x = 0
while x < 10:
    new_ice_cream_stand.increment_number_served(1)
    print(f"\nNow served {new_ice_cream_stand.number_served} customers")
    x += 1