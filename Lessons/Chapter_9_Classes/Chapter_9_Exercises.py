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

# #9.6
# class Restaurant:
#     """ A simple attempt to represent a restaurant """
#     def __init__(self, name, cuisine):
#         """ Initialize atrributes of restaurant """
#         self.name = name.title()
#         self.cuisine = cuisine.title()
#         self.number_served = 50


#     def describe_restaurant(self):
#         """ return a neatly formatted opening message """
#         opening_message = f"\n{self.name} is now open " + \
#                           f"\nServing great {self.cuisine} " + \
#                           f"to {self.number_served} customers and counting"
#         return opening_message


#     def set_number_served(self, number_served):
#         """Add a given amount to the number of people served"""
#         self.number_served = number_served


#     def increment_number_served(self, additional_number_served):
#         """ increment the number of people served by a given amount"""
#         self.number_served += additional_number_served


# class IceCreamStand(Restaurant):
#     """ Ice cream stands are a special type of restaurant"""

#     def __init__(self, name, cuisine='Ice Cream'):
#         """
#         Initialize atrributes of parent restaurant
#         and then initialize attributes specific to Ice Creaam Stand
#         """
#         super().__init__(name, cuisine)
#         self.ice_cream_flavours = []


#     def describe_flavours(self):
#         """ returns formatted list of flavours"""
#         print("\nWe have the following flavors available:")
#         for flavour in self.flavours:
#             print(f"\t- {flavour.title()}")


# new_ice_cream_stand = IceCreamStand('Gelato')
# new_ice_cream_stand.flavours = ['vanilla', 'chocalate', 'strawberry', 'matcha tea', 'bubble gum']
# print(new_ice_cream_stand.describe_restaurant())
# new_ice_cream_stand.describe_flavours()

# x = 0
# while x < 10:
#     new_ice_cream_stand.increment_number_served(1)
#     print(f"\nNow served {new_ice_cream_stand.number_served} customers")
#     x += 1

#9.7
# class User:
#     """ A simple user class """
#     def __init__(self, user_name, first_name, last_name, location):
#         self.user_name = user_name
#         self.first_name = first_name
#         self.last_name = last_name
#         self.location = location
#         self.login_attempts = 0


#     def describe_user(self):
#         description =   f"Username:\t{self.user_name}" + \
#                         f"\nFirst Name:\t{self.first_name.title()}" + \
#                         f"\nLast Name:\t{self.last_name.title()}" + \
#                         f"\nLocation:\t{self.location.title()}" + \
#                         f"\nLogin Attempts:\t{self.login_attempts}"
#         print(description)


#     def reset_login_attempts(self):
#         self.login_attempts = 0


#     def increment_login_attempts(self):
#         self.login_attempts += 1

# class Administrator(User):
#     """Describes a special type of user"""
#     def __init__(self, user_name, first_name, last_name, location):
#         """Initialize atrributes of User and then attributes of Administrator"""
#         super().__init__(user_name, first_name, last_name, location)
#         self.privileges = Privileges()


# class Privileges():
#     """Assign and show priviliges asssigned to a user"""
#     def __init__(self, privileges=[]):
#         """ initialise the priviliges attribute"""
#         self.privileges = privileges

#     def show_privileges(self):
#         """Shows the priviliges the user has"""
#         if self.privileges:
#             print("\nPrivileges")
#             for privilege in self.privileges:
#                 print(f"\t- {privilege.title()}")
#         else:
#             print("You have no privileges")


# john = Administrator('john.doe@email.com','John', 'Doe', 'Perth')
# john.describe_user()
# print("\nAdding Privileges")
# john.privileges.privileges = ['add user', 'delete user', 'modify user', 'reset password']

# john.privileges.show_privileges()
# print('\nPrivileges have been updated')
# john.privileges.privileges.append('delete posts')
# john.privileges.show_privileges()

#9.9
# class Car():
#     """A simple attempt to represent a car."""

#     def __init__(self, manufacturer, model, year):
#         """Initialize attributes to describe a car."""
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class Battery():
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=75):
#         """Initialize the batteery's attributes."""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         distance = int(self.battery_size) * 2
#         range = distance

#         message = f"This car can go approximately {range}"
#         message += " kms on a full charge."
#         print(message)

#     def upgrade_battery(self):
#         if self.battery_size < 100:
#             new_battery_size = 100

#             print(f"Battery has been upgraded from {self.battery_size}" + \
#             f" to {new_battery_size} kWh")
#             self.battery_size = new_battery_size
#         else:
#             print(f"Battery already upgraded to {self.battery_size} kWh")


# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""

#     def __init__(self, manufacturer, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(manufacturer, model, year)
#         self.battery = Battery()


# print("Make an electric car, and check the range:")
# my_tesla = ElectricCar('tesla', 'roadster', 2019)
# my_tesla.battery.battery_size = 10
# my_tesla.battery.get_range()

# print("\nUpgrade the battery, and check the range again:")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()