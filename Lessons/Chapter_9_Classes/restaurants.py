"""
A set of classes that can be used to describe a restaurant
"""
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

        super().__init__(name, cuisine)
        self.ice_cream_flavours = []


    def describe_flavours(self):
        """ returns formatted list of flavours"""
        print("\nWe have the following flavors available:")
        for flavour in self.ice_cream_flavours:
            print(f"\t- {flavour.title()}")


